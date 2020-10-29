from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm,LoginForm,ProfileModelForm
from .models import Profile,Relationship
from posts.models import Post
from django.urls import reverse

# Create your views here.


#profile function 
def profile(request,profileId):
    if request.user.is_authenticated:
        # profile = Profile.objects.get(user=request.user)
        profile = Profile.objects.get(id=profileId)
        form = ProfileModelForm(request.POST or None, request.FILES or None , instance=profile)
        posts = Post.objects.filter(author=profile)
        # print(posts)
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
        }
        return render(request,'users/profile.html',context)
    else:
        return redirect('users:login')

#signup function
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'SignUp Done !! You can login now')
            form.save()
            return HttpResponseRedirect('../login')
    else:        
        form = SignUpForm()
    return render(request,'users/signup.html',{'form':form})


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
                    messages.success(request,"Logged in Successfully !! ")
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
        return render(request,'users/login.html',{'form':form})
    else:
        messages.info(request,'You are logged in now !! ')
        return HttpResponseRedirect('/')


#user logout function
def user_logout(request):
    logout(request)
    messages.success(request,'Logout Successfully!!')
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
        }
        return render(request,'users/changepass.html',context)