from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm,LoginForm,ProfileModelForm
from .models import Profile,Relationship
from posts.models import Post
from blog.models import Blog
from pastebin.models import Pastebindb
from archive.models import Solution
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import validators
from django import forms


from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
UserModel = get_user_model()
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
        solutions = Solution.objects.filter(author=profile)
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
            'solutions':solutions,
            'active':'active',
        }
        return render(request,'users/profile.html',context)
    else:
        return redirect('users:login')

#signup function
# def signup(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect('../login')
#             return redirect('users:login')
#     else:        
#         form = SignUpForm()

#     context = {
#         'form':form,
#         'active':'active',
#     }
#     return render(request,'users/signup.html',context)

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_email = form.cleaned_data['email']

            if  User.objects.filter(email=user_email).exists():
                messages.info(request,'Email is already used.Try with another one')
                return redirect('users:signup')

            user = form.save(commit=False)
            # return HttpResponseRedirect('../login')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Active Your Account'
            # Mail body making
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            domain = get_current_site(request).domain
            link = reverse('users:activate',kwargs={'uidb64':uidb64,'token':token})
            activate_url = 'http://'+domain+link

            mail_body = 'Hi '+user.username + ',\nPlease click the link below to activate your account \n'+activate_url
            user_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject,
                mail_body,
                to=[user_email]
            )
            email.send()
            messages.success(request,'check your mail and active your account')
            return redirect('users:login')
    else:        
        form = SignUpForm()

    context = {
        'form':form,
        'active':'active',
    }
    return render(request,'users/signup.html',context)


# class SignupView(View):
#     def post(self,request):
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
        
#         form = SignUpForm()
#         context = {
#             'form':form,
#             'active':'active',
#         }
#         return render(request,'users/signup.html',context)
#     def get(self,request):
#         form = SignUpForm()
#         context = {
#             'form':form,
#             'active':'active',
#         }
#         return render(request,'users/signup.html',context)


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





    
def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user =  UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request,'Your account is activated')
        return redirect('users:login')
    else:
        messages.info(request,'Oops!! Activation link is invalid')
        return redirect('users:login')
