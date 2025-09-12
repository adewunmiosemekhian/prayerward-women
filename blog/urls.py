# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('categories/', views.categories, name='categories'),
    path('posts/', views.all_posts, name='all_posts'),
    path('contact/', views.contact, name='contact'),
]