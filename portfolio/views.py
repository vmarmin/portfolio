from django.shortcuts import render
from blog.models import Post

def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': featured,
        'latest': latest
    }
    return render(request, 'index.html', context)
