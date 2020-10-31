from django.urls import path
from .import views

app_name = 'posts'

urlpatterns = [
    path('allposts/',views.list_all_post_comments,name='allposts'),
    path('like/',views.like_comment_post,name='postsLike'),
    path('delete/<pk>/',views.PostDelete,name='postsDelete'),
    path('update/<pk>/',views.PostUpdate,name='postsUpdate'),
    path('details/<pk>',views.PostDetails,name='postsDetails'),
    path('delete/<pk>/<postid>/',views.commentDelete,name='commentDelete'),
    path('edit/<pk>/<postid>/',views.commentEdit,name='commentEdit'), 
    path('search/',views.search_post,name='search_post'),  
]
