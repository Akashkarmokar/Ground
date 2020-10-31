from django.shortcuts import render,redirect
from .models import Blog,blogComment,blogRead
from users.models import Profile
from .forms import CreateBlogModelForm,blogCommentModalForm,CategoryModelForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
# Create your views here.


def blog(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            blog_create_form=CreateBlogModelForm(request.POST or None)
            profile = Profile.objects.get(user=request.user)
            if blog_create_form.is_valid():
                instance = blog_create_form.save(commit=False)
                instance.author = profile
                instance.save()
                CreateBlogModelForm()
                blog_obj=Blog.objects.all()
                blog_create_form = CreateBlogModelForm()
                context = {
                    'blog_obj':blog_obj,
                    'blog_create_form':blog_create_form,
                    'active':'active',
                }
                return render(request,'blog/blog.html',context)
        else:
            return redirect('users:login')
    else:
        blog_obj=Blog.objects.all()
        blog_create_form = CreateBlogModelForm()
        context = {
            'blog_obj':blog_obj,
            'blog_create_form':blog_create_form,
            'active':'active',
        }
    return render(request, 'blog/blog.html',context)

def blog_details(request,pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if 'read_more' in request.POST:
                blog_obj = Blog.objects.get(pk=pk)
                comment_form = blogCommentModalForm()
                current_User = request.user
                blog_Id = request.POST.get('read_more')
                profile_obj = Profile.objects.get(user=current_User)

                if profile_obj not in blog_obj.read.all():
                    blog_obj.read.add(profile_obj)

                read, created = blogRead.objects.get_or_create(user=profile_obj,blog_id=blog_Id)
                if created:
                    read.value = 'Read'
                blog_obj.save()
                read.save()
                context = {
                    'blog_obj':blog_obj,
                    'comment_form':comment_form,
                    'active':'active',
                }
                return render(request, 'blog/blog-details.html',context)

            if 'comment_submit_form' in request.POST:
                comment_form = blogCommentModalForm(request.POST or None)
                profile = Profile.objects.get(user=request.user)
                if comment_form.is_valid():
                    instance = comment_form.save(commit=False)
                    instance.user = profile
                    instance.blog = Blog.objects.get(id = request.POST.get('blog_id'))
                    instance.save()
                    blog_obj = Blog.objects.get(pk=pk)
                    comment_form = blogCommentModalForm()
                    context = {
                        'blog_obj':blog_obj,
                        'comment_form':comment_form,
                        'active':'active',
                    }
                    return render(request, 'blog/blog-details.html',context)    
        else:
            return redirect('users:login')
    else:
        blog_obj = Blog.objects.get(pk=pk)
        comment_form = blogCommentModalForm()
        context = {
            'blog_obj':blog_obj,
            'comment_form':comment_form,
            'active':'active',
        }
        return render(request, 'blog/blog-details.html',context)    



def create_blog(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if 'category_submit_form' in request.POST:
                created_category = CategoryModelForm(request.POST or None)
                if created_category.is_valid():
                    created_category.save()
                    return redirect('blog:create_blog')
            if 'blog_submit_form' in request.POST:
                blog_create_form=CreateBlogModelForm(request.POST or None)
                profile = Profile.objects.get(user=request.user)
                if blog_create_form.is_valid():
                    instance = blog_create_form.save(commit=False)
                    instance.author = profile
                    instance.save()
                    CreateBlogModelForm()
                    blog_obj=Blog.objects.all()
                    blog_create_form = CreateBlogModelForm()
                    context = {
                        'blog_obj':blog_obj,
                        'blog_create_form':blog_create_form,
                        'active':'active',
                    }
                    return render(request,'blog/blog.html',context)
        else:
            return redirect('users:login')
    else:
        blog_create_form = CreateBlogModelForm()
        category_form = CategoryModelForm()
        context = {
            'blog_create_form':blog_create_form,
            'category_form':category_form,
            'active':'active',
        }
        return render(request,'blog/createBlog.html',context)


def delete_blog(request,pk):
    if request.user.is_authenticated:
        try:
            obj = Blog.objects.get(pk=pk)
            if obj.author.user == request.user:
                obj.delete()
                return redirect('blog:all_blog')
            else:
                return render(request,'home/error.html') 
        except Blog.DoesNotExist:
            return render(request,'home/error.html') 
    else:
        return redirect('users:login')


def update_blog(request,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                obj = Blog.objects.get(pk=pk)
                if obj.author.user == request.user:
                    if 'category_submit_form' in request.POST:
                        created_category = CategoryModelForm(request.POST or None)
                        if created_category.is_valid():
                            created_category.save()
                            return redirect('blog:update_blog')
                    form = CreateBlogModelForm(request.POST,instance=obj)
                    if form.is_valid():
                        form.save()
                        form = CreateBlogModelForm()
                        context = {
                            'form':form,
                        }
                        return redirect(reverse('blog:single_blog',args=pk))
            except Blog.DoesNotExist:
                return render(request,'home/error.html')
        else:
            try:
                obj = Blog.objects.get(pk=pk)
                if obj.author.user == request.user:
                    form = CreateBlogModelForm(instance=obj)
                    category_form = CategoryModelForm()
                    context={
                        'form':form,
                        'category_form':category_form,
                        'active':'active',
                    }
                    return render(request,'blog/updateBlog.html',context)
            except Blog.DoesNotExist:
                return render(request,'home/error.html')
    else:
        return redirect('users:login')


# ////////////////// Comment Section ///////////////////

def delete_comment(request,pk,postid):
    if request.user.is_authenticated:
        print(postid)
        try:
            obj = blogComment.objects.get(pk=pk)
            if obj.user.user == request.user:
                obj.delete()
                return redirect(reverse('blog:single_blog',args=postid))
            else:
                return render(request,'home/error.html')
        except blogComment.DoesNotExist:
            return render(request,'home/error.html')
    else:
        return redirect('users:login')



def update_comment(request,pk,postid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                obj = blogComment.objects.get(pk=pk)
                if obj.user.user == request.user:
                    form = blogCommentModalForm(request.POST,instance=obj)
                    if form.is_valid():
                        form.save()
                        return redirect(reverse('blog:single_blog',args=postid))
                else:
                    return render(request,'home/error.html')
            except blogComment.DoesNotExist:
                return render(request,'home/error.html') 
        else:
            try:
                obj = blogComment.objects.get(pk=pk)
                if obj.user.user == request.user:
                    form = blogCommentModalForm(instance=obj)
                    context={
                        'form':form,
                        'active':'active',
                    }
                    return render(request,'blog/update_comment.html',context)
            except blogComment.DoesNotExist:
                return render(request,'home/error.html') 
    else:
        return redirect('users:login')