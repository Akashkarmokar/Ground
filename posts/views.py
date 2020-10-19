from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Post,Like
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from users.forms import LoginForm
from users.models import Profile
from .forms import PostModelForm,CommentModelForm
from django.contrib import messages

# Create your views here.

def list_all_post_comments(request):
    all_posts = Post.objects.all()
    profile = Profile.objects.get(user=request.user)

    # Post form, Comment form 
    post_form = PostModelForm()
    comment_form = CommentModelForm()
    
    if 'post_submit_form' in request.POST:
        post_form = PostModelForm(request.POST or None,request.FILES or None)
        if post_form.is_valid():
            instance =  post_form.save(commit=False)
            instance.author = profile 
            instance.save()
            post_form = PostModelForm()
            messages.success(request,'Your Post successfully posted')
    if 'comment_submit_form' in request.POST:
        comment_form = CommentModelForm(request.POST or None)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id = request.POST.get('post_id'))
            instance.save()
            comment_form = CommentModelForm()
            messages.success(request,'Comment Added')

    
    context={
        'all_posts':all_posts,
        'profile':profile,
        'post_form':post_form,
        'comment_form':comment_form,
    }
    return render(request,'posts/listPost.html',context)



def like_comment_post(request):
    if request.user.is_authenticated:
        currentUser = request.user
        if request.method == 'POST':
            postId = request.POST.get('post_id')
            postObj = Post.objects.get(id=postId)
            profileObj = Profile.objects.get(user=currentUser)

            if profileObj in postObj.liked.all():
                postObj.liked.remove(profileObj)
            else:
                postObj.liked.add(profileObj)

            like, created = Like.objects.get_or_create(user=profileObj,post_id=postId)
            if not created:
                if like.value == 'Like':
                    like.value = 'Unlike'
                else:
                    like.value = 'Like'
                postObj.save()
                like.save()
        return redirect('posts:allposts')
    
    else:
        messages.success(request,"Login First ...!!")
        return HttpResponseRedirect('/user/login/')