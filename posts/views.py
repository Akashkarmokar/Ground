from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import Http404
from .models import Post,Like,Comment
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from users.forms import LoginForm
from users.models import Profile
from .forms import PostModelForm,CommentModelForm
from django.contrib import messages
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy ,reverse

# Create your views here.

def list_all_post_comments(request):
    if request.method == "POST":
        if request.user.is_authenticated:
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
                    messages.success(request,'Your Post successfully posted')
            if 'comment_submit_form' in request.POST:
                comment_form = CommentModelForm(request.POST or None)
                if comment_form.is_valid():
                    instance = comment_form.save(commit=False)
                    instance.user = profile
                    instance.post = Post.objects.get(id = request.POST.get('post_id'))
                    instance.save()
                    messages.success(request,'Comment Added')

            post_form = PostModelForm()
            comment_form = CommentModelForm()
            context={
                'all_posts':all_posts,
                'profile':profile,
                'post_form':post_form,
                'comment_form':comment_form,
            }
            return render(request,'posts/listPost.html',context)
        else:
            messages.info(request,"Login First.......!")
            return HttpResponseRedirect('/user/login')
    else:
        all_posts = Post.objects.all()
        post_form = PostModelForm()
        comment_form = CommentModelForm()
        context={
            'all_posts':all_posts,
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
            else:
                like.value = 'Like'
                
                postObj.save()
                like.save()
        return redirect('posts:allposts')
    
    else:
        messages.success(request,"Login First ...!!")
        return HttpResponseRedirect('/user/login/')


def PostDelete(request,pk):
    if request.user.is_authenticated:
        try:
            obj = Post.objects.get(pk=pk)
            if obj.author.user == request.user:
                obj.delete()
                return redirect('posts:allposts')
            else:
                messages.warning(request,"You are not the author of this post")
                return redirect('posts:allposts')
        except Post.DoesNotExist:
            raise Http404("Your link is Wrong or it is not available.Here") 
    else:
        messages.info(request,"Login First............!")
        return redirect('users:login')


def PostUpdate(request,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                obj = Post.objects.get(pk=pk)
                if obj.author.user == request.user:
                    form = PostModelForm(request.POST,instance=obj)
                    if form.is_valid():
                        form.save()
                        obj = form.save()
                        obj.save()
                        context = {
                            'form':form,
                        }
                        return redirect(reverse('posts:postsDetails',args=pk))
                else:
                    messages.warning(request,"You are not the author of this post")
                    return redirect('posts:allposts')
            except Post.DoesNotExist:
                raise Http404("Your link is Wrong or it is not available.Here")

        else:
            try:
                obj = Post.objects.get(pk=pk)
                if obj.author.user == request.user:
                    form = PostModelForm(instance=obj)
                    context = {
                        'form':form,
                    }
                    return render(request,'posts/update.html',context)
                else:
                    messages.warning(request,"You are not the author of this post")
                    return redirect('posts:allposts')
            except Post.DoesNotExist:
                raise Http404("Your link is Wrong or it is not available.Here") 
    else:
        messages.info(request,"Login First............!")
        return redirect('users:login')


def PostDetails(request,pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if 'comment_submit_form' in request.POST:
                comment_form = CommentModelForm(request.POST or None)
                profile = Profile.objects.get(user=request.user)
                if comment_form.is_valid():
                    instance = comment_form.save(commit=False)
                    instance.user = profile
                    instance.post = Post.objects.get(id = request.POST.get('post_id'))
                    instance.save()
                    messages.success(request,'Comment Added')
                    obj = Post.objects.get(pk=pk)
                    comment_form = CommentModelForm()
                    context = {
                        'post':obj,
                        'comment_form':comment_form,
                    }
                    return render(request,'posts/post_details.html',context)
        else:
            messages.info(request,"Login First............!")
            return redirect('users:login')
    else:
        obj = Post.objects.get(pk=pk)
        comment_form = CommentModelForm()
        context = {
            'post':obj,
            'comment_form':comment_form,
        }
        return render(request,'posts/post_details.html',context)



#///////////////////////////  Comment section ////////////////////////////////////



def commentEdit(request,pk,postid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                obj = Comment.objects.get(pk=pk)
                if obj.user.user == request.user:
                    form = CommentModelForm(request.POST,instance=obj)
                    if form.is_valid():
                        form.save()
                        obj = form.save()
                        obj.save()
                        context = {
                            'form':form,
                        }
                        return redirect(reverse('posts:postsDetails',args=postid))
                else:
                    messages.warning(request,"You are not the author of this post")
                    return redirect('posts:allposts')
            except Post.DoesNotExist:
                raise Http404("Your link is Wrong or it is not available.Here")

        else:
            try:
                obj = Comment.objects.get(pk=pk)
                if obj.user.user == request.user:
                    form = CommentModelForm(instance=obj)
                    context = {
                        'form':form,
                    }
                    return render(request,'posts/commentEdit.html',context)
                else:
                    messages.warning(request,"You are not the author of this post")
                    return redirect('posts:allposts')
            except Post.DoesNotExist:
                raise Http404("Your link is Wrong or it is not available.Here") 
    else:
        messages.info(request,"Login First............!")
        return redirect('users:login')






def commentDelete(request,pk,postid):
    if request.user.is_authenticated:
        try:
            obj = Comment.objects.get(pk=pk)
            if obj.user.user == request.user:
                obj.delete()
                post_obj = Post.objects.get(pk=postid)
                comment_form = CommentModelForm()
                context = {
                    'post':post_obj,
                    'comment_form':comment_form,
                }
                return redirect(reverse('posts:postsDetails',args=postid))
            else:
                messages.warning(request,"You are not the author of this post")
                return redirect('posts:allposts')
        except Comment.DoesNotExist:
            raise Http404("Your link is Wrong or it is not available.Here") 
    else:
        messages.info(request,"Login First............!")
        return redirect('users:login')
