from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,LoginForm


# Create your views here.


def home(request):
    return render(request,'home/home.html')

#signup function
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'SignUp Done !! . You can login now')
            form.save()
            return HttpResponseRedirect('/')
    else:        
        form = SignUpForm()
    return render(request,'home/signup.html',{'form':form})


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
        return render(request,'home/login.html',{'form':form})
    else:
        messages.info(request,'You are logged in now !! ')
        return HttpResponseRedirect('/')


#user profile function
def profile(request):
    return render(request,'home/profile.html')

#user logout function
def user_logout(request):
    logout(request)
    messages.success(request,'Logout Successfully!!')
    return HttpResponseRedirect('/')