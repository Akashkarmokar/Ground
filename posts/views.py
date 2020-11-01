from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import Http404
from .models import Post,Like,Comment
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from users.forms import LoginForm
from users.models import Profile
from .forms import PostModelForm,CommentModelForm
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy ,reverse
from django.contrib.auth.models import User
from home.models import Feedback
from django.db.models import Q
from blog.models import Blog

# Create your views here.

def list_all_post_comments(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            all_posts = Post.objects.all()
            all_blogs = Blog.objects.all()
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
            if 'comment_submit_form' in request.POST:
                comment_form = CommentModelForm(request.POST or None)
                if comment_form.is_valid():
                    instance = comment_form.save(commit=False)
                    instance.user = profile
                    instance.post = Post.objects.get(id = request.POST.get('post_id'))
                    instance.save()

            post_form = PostModelForm()
            comment_form = CommentModelForm()


            total_post_num = all_posts.count()
            total_blog_num = all_blogs.count()
            total_user_num = User.objects.all().count()
            total_feedback_num = Feedback.objects.all().count()

            context={
                'all_posts':all_posts,
                'profile':profile,
                'post_form':post_form,
                'comment_form':comment_form,
                'total_post':total_post_num,
                'total_blog':total_blog_num,
                'total_user':total_user_num,
                'total_feedback':total_feedback_num,
                'active':'active',
            }
            return render(request,'posts/listPost.html',context)
        else:
            return HttpResponseRedirect('/user/login')
    else:
        all_posts = Post.objects.all()
        all_blogs = Blog.objects.all()
        recent_blogs = Blog.objects.all()[:10]
        post_form = PostModelForm()
        comment_form = CommentModelForm()


        total_post_num = all_posts.count()
        total_blog_num = all_blogs.count()
        total_user_num = User.objects.all().count()
        total_feedback_num = Feedback.objects.all().count()
        context={
            'all_posts':all_posts,
            'recent_blogs':recent_blogs,
            'post_form':post_form,
            'comment_form':comment_form,
            'total_post':total_post_num,
            'total_blog':total_blog_num,
            'total_user':total_user_num,
            'total_feedback':total_feedback_num,
            'active':'active',
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
        return HttpResponseRedirect('/user/login/')


def PostDelete(request,pk):
    if request.user.is_authenticated:
        try:
            obj = Post.objects.get(pk=pk)
            if obj.author.user == request.user:
                obj.delete()
                return redirect('posts:allposts')
            else:
                return redirect('posts:allposts')
        except Post.DoesNotExist:
            raise Http404("Your link is Wrong or it is not available.Here") 
    else:
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
                            'active':'active',
                        }
                        return redirect(reverse('posts:postsDetails',args=pk))
                else:
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
                        'active':'active',
                    }
                    return render(request,'posts/update.html',context)
                else:
                    return redirect('posts:allposts')
            except Post.DoesNotExist:
                raise Http404("Your link is Wrong or it is not available.Here") 
    else:
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
                    obj = Post.objects.get(pk=pk)
                    comment_form = CommentModelForm()
                    context = {
                        'post':obj,
                        'comment_form':comment_form,
                        'active':'active',
                    }
                    return render(request,'posts/post_details.html',context)
        else:
            return redirect('users:login')
    else:
        obj = Post.objects.get(pk=pk)
        comment_form = CommentModelForm()
        context = {
            'post':obj,
            'comment_form':comment_form,
            'active':'active',
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
                            'active':'active',
                        }
                        return redirect(reverse('posts:postsDetails',args=postid))
                else:
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
                        'active':'active',
                    }
                    return render(request,'posts/commentEdit.html',context)
                else:
                    return redirect('posts:allposts')
            except Post.DoesNotExist:
                raise Http404("Your link is Wrong or it is not available.Here") 
    else:
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
                    'active':'active',
                }
                return redirect(reverse('posts:postsDetails',args=postid))
            else:
                return redirect('posts:allposts')
        except Comment.DoesNotExist:
            raise Http404("Your link is Wrong or it is not available.Here") 
    else:
        return redirect('users:login')




# ////////////////////           Post Search  ////////////////////////

def search_post(request):
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
            if 'comment_submit_form' in request.POST:
                comment_form = CommentModelForm(request.POST or None)
                if comment_form.is_valid():
                    instance = comment_form.save(commit=False)
                    instance.user = profile
                    instance.post = Post.objects.get(id = request.POST.get('post_id'))
                    instance.save()

            post_form = PostModelForm()
            comment_form = CommentModelForm()


            total_post_num = all_posts.count()
            total_user_num = User.objects.all().count()
            total_feedback_num = Feedback.objects.all().count()

            context={
                'all_posts':all_posts,
                'profile':profile,
                'post_form':post_form,
                'comment_form':comment_form,
                'total_post':total_post_num,
                'total_user':total_user_num,
                'total_feedback':total_feedback_num,
                'active':'active',
            }
            return render(request,'posts/listPost.html',context)
        else:
            return HttpResponseRedirect('/user/login')
    else:
        # all_posts = Post.objects.all()
        query = request.GET['query']
        all_posts = Post.objects.filter(Q(heading__icontains=query)|Q(author__user__username__icontains=query))
        post_form = PostModelForm()
        comment_form = CommentModelForm()


        total_post_num = all_posts.count()
        total_user_num = User.objects.all().count()
        total_feedback_num = Feedback.objects.all().count()
        context={
            'all_posts':all_posts,
            'post_form':post_form,
            'comment_form':comment_form,
            'total_post':total_post_num,
            'total_user':total_user_num,
            'total_feedback':total_feedback_num,
            'active':'active',
        }
        return render(request,'posts/listPost.html',context)

