from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout
# from posts.models import Post,Comment
# from django.urls import reverse
from .models import Feedback
from .forms import FeedbackForm
from users.models import Profile
from django.contrib.auth.models import User
from django.db.models import Q
from blog.models import Blog
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('posts:allposts')
    else:
        obj = Feedback.objects.all()[:4]
        recent_blogs = Blog.objects.all()[:3]
        context = {
            'feedbacks':obj,
            'recent_blogs':recent_blogs,
            'active':'active',
        }
        return render(request,'home/home.html',context)


def user_search(request):
    query = request.GET['query']
    min_length = True
    if len(query) > 50 :
        min_length = False
        all_user = User.objects.none()
    else:
        all_user = User.objects.filter(Q(id__icontains=query)|Q(username__icontains=query))
    context = {
        'all_user':all_user,
        'min_length':min_length,
        'query':query,
    }
    return render(request,'home/search_user.html',context)




def feedback(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            feedbackObj=FeedbackForm(request.POST)
            profile = Profile.objects.get(user=request.user)
            if feedbackObj.is_valid():
                instance=feedbackObj.save(commit=False)
                instance.author = profile
                instance.save()
                return redirect('home_url')
        else:
            return redirect('users:login')

    else:
        obj = FeedbackForm()
        feedbacks = Feedback.objects.all()
        context = {
            'form':obj,
            'feedbacks':feedbacks,
        }
        return render(request,'home/feedback.html',context)


def privecy(request):
    return render(request,'home/privecy.html')

def terms_condition(request):
    return render(request,'home/terms_condition.html')


def developer(request):
    return render(request,'home/developer.html')