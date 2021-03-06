from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import CommentForm, PostForm
from .models import AnonPostView, Author, Post, PostView


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def blog(request):
    category_count = get_category_count()
    tag_count = get_tag_count()
    post_list = Post.objects.all()
    most_recent = Post.objects.order_by("-timestamp")[:3]
    paginator = Paginator(post_list, per_page=4)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        "queryset": paginated_queryset,
        "most_recent": most_recent,
        "page_request_var": page_request_var,
        "category_count": category_count,
        "tag_count": tag_count,
    }
    return render(request, "blog.html", context)


def post(request, id):
    post = get_object_or_404(Post, id=id)
    category_count = get_category_count()
    tag_count = get_tag_count()
    most_recent = Post.objects.order_by("-timestamp")[:3]
    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)
    else:
        AnonPostView.objects.create(post=post)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post", kwargs={"id": post.id}))
    context = {
        "post": post,
        "category_count": category_count,
        "most_recent": most_recent,
        "tag_count": tag_count,
        "form": form,
    }
    return render(request, "post.html", context)


def get_category_count():
    queryset = Post.objects.values("categories__title").annotate(
        Count("categories__title")
    )
    return queryset


def get_tag_count():
    queryset = Post.objects.values("tags__title").annotate(Count("tags__title"))
    return queryset


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(overview__icontains=query)
        ).distinct()
    context = {
        "queryset": queryset,
    }
    return render(request, "search_result.html", context)


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post", kwargs={"id": form.instance.id}))
    context = {"form": form, "title": "Create post"}
    return render(request, "post_create.html", context)


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post", kwargs={"id": form.instance.id}))
    context = {"form": form, "title": "Update post"}
    return render(request, "post_create.html", context)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("blog"))
