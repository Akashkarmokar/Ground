from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout
# from posts.models import Post,Comment
# from django.urls import reverse
from .models import Feedback
from .forms import FeedbackForm
from users.models import Profile
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('posts:allposts')
    else:
        obj = Feedback.objects.all()
        context = {
            'feedbacks':obj,
        }
        return render(request,'home/home.html')


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