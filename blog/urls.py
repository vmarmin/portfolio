from django.urls import path

from .views import blog, post, post_create, post_delete, post_update, search

urlpatterns = [
    path("", blog, name="blog"),
    path("post/<id>/", post, name="post"),
    path("create/", post_create, name="post-create"),
    path("post/<id>/update/", post_update, name="post-update"),
    path("post/<id>/delete/", post_delete, name="post-delete"),
    path("search/", search, name="search"),
]
