from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def blog(request):
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
    }
    return render(request, "blog.html", context)


def post(request):
    return render(request, "post.html", {})
