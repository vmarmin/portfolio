from django.contrib import admin

from .models import Author, Category, Post, Tag, Comment, PostView

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
