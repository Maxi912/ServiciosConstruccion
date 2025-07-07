
from django.urls import path
from .views import about_view, blog_list, blog_detail, blog_create, blog_update, blog_delete

urlpatterns = [
    path('about/', about_view, name='about'),
    path('pages/', blog_list, name='blog_list'),
    path('pages/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('create/', blog_create, name='blog_create'),
    path('edit/<int:blog_id>/', blog_update, name='blog_update'),
    path('delete/<int:blog_id>/', blog_delete, name='blog_delete'),
]