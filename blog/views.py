from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


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
    context = {
        'post': post,
        "category_count": category_count,
        "most_recent": most_recent,
        "tag_count": tag_count,
    }
    return render(request, "post.html", context)


def latest(request):
    post = Post.objects.order_by('-timestamp')[0]
    return redirect(post.get_absolute_url())


def get_category_count():
    queryset = Post.objects.values("categories__title").annotate(Count("categories__title"))
    return queryset


def get_tag_count():
    queryset = Post.objects.values("tags__title").annotate(Count("tags__title"))
    return queryset


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
    }
    return render(request, "search_result.html", context)
