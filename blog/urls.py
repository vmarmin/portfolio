from django.urls import path
from .views import blog, post, search

urlpatterns = [
    path('', blog, name='blog'),
    path('post/<id>/', post, name='post'),
    path('search/', search, name='search'),
]
