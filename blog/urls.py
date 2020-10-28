from django.urls import path
from .import views

app_name='blog'

urlpatterns = [
    path('main/',views.blog,name="all_blog"),
    path('blog-details/',views.blog_details,name="single_blog"),
]
