from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm,LoginForm,ProfileModelForm
from .models import Profile,Relationship
from posts.models import Post
from blog.models import Blog
from pastebin.models import Pastebindb
from django.urls import reverse

# Create your views here.


#profile function 
def profile(request,profileId):
    if request.user.is_authenticated:
        # profile = Profile.objects.get(user=request.user)
        profile = Profile.objects.get(id=profileId)
        form = ProfileModelForm(request.POST or None, request.FILES or None , instance=profile)
        posts = Post.objects.filter(author=profile)
        blogs = Blog.objects.filter(author=profile)
        pastebins = Pastebindb.objects.filter(user=profile)
        update_confirm = False

        if request.method == "POST":
            if form.is_valid():
                form.save()
                update_confirm = True

        context = {
            'profile':profile,
            'form':form,
            'update_confirm':update_confirm,
            'posts':posts,
            'blogs':blogs,
            'pastebins':pastebins,
            'active':'active',
        }
        return render(request,'users/profile.html',context)
    else:
        return redirect('users:login')

#signup function
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('../login')
            return redirect('users:login')
    else:        
        form = SignUpForm()
        context = {
            'form':form,
            'active':'active',
        }
    return render(request,'users/signup.html',context)


#user login function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user_obj = authenticate(username=uname,password=upass)
                if user_obj is not None:
                    login(request,user_obj)
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
            context = {
                'form':form,
                'active':'active',
            }
        return render(request,'users/login.html',context)
    else:
        return HttpResponseRedirect('/')


#user logout function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


#user Password Change
def changepass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('posts:allposts')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form':form,
            'active':'active',
        }
        return render(request,'users/changepass.html',context)