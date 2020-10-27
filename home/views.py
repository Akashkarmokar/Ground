from django.shortcuts import render,HttpResponseRedirect,redirect
# from posts.models import Post,Comment
# from django.urls import reverse
from .models import Feedback
from .forms import FeedbackForm
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('posts:allposts')
    else:
        return render(request,'home/home.html')


def feedback(request):
    if request.method == 'POST':
        feedbackObj=FeedbackForm(request.POST)
        if feedbackObj.is_valid():
            feedbackObj.save()
            return redirect('home_url')

    else:
        obj = FeedbackForm()
        context = {
            'form':obj,
        }
        return render(request,'home/feedback.html',context)