from django.shortcuts import render
from blog.models import Post
from marketing.models import Signup


def index(request):
    featured = Post.objects.filter(featured=True).order_by("-timestamp")
    latest = Post.objects.order_by("-timestamp")[0:3]
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {"object_list": featured, "latest": latest}

    return render(request, "index.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)
