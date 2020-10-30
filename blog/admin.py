from django.contrib import admin

from .models import Author, Category, Comment, Post, PostView, Tag

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
