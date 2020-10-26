from django.shortcuts import render
from posts.models import Post,Comment
# Create your views here.


def home(request):
    all_posts=Post.objects.all()
    context={
        'all_posts':all_posts
    }

    return render(request,'home/home.html',context)
