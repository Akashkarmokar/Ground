from django.urls import path
from .import views

app_name='blog'

urlpatterns = [
    path('main/',views.blog,name="all_blog"),
    path('blog-details/<pk>/',views.blog_details,name="single_blog"),
    path('create_blog/',views.create_blog,name="create_blog"),
    path('delete_blog/<pk>/',views.delete_blog,name='delete_blog'),
    path('update_blog/<pk>/',views.update_blog,name='update_blog'),

    path('delete_comment/<pk>/<postid>/',views.delete_comment,name='delete_comment'),
    path('update_comment/<pk>/<postid>/',views.update_comment,name='update_comment'),

    path('search/',views.blog_search,name='blog_search')
]
