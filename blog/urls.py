from django.urls import path
from .views import blog, post, search, latest

urlpatterns = [
    path('', blog, name='blog'),
    path('post/<id>/', post, name='post'),
    path('post/latest', latest, name='latest'),
    path('search/', search, name='search'),
]
