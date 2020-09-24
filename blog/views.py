from django.shortcuts import render

def blog(request):
    return render(request, 'blog.html', {})

def post(request):
    return render(request, 'post.html', {})
