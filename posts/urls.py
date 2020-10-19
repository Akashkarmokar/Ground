from django.urls import path
from .import views

app_name = 'posts'

urlpatterns = [
    path('allposts/',views.list_all_post_comments,name='allposts'),
    path('like/',views.like_comment_post,name='postsLike'),
]
