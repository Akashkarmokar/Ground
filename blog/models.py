from django.db import models
from users.models import Profile
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


# Blog Model
class Blog(models.Model):
    title = models.CharField(max_length=250)
    # content = models.TextField()
    content = RichTextField()
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)
    read = models.ManyToManyField(Profile,blank=True,related_name='reads')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='blogs')


    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def num_comments(self):
        return self.blogcomment_set.all().count()

    class Meta:
        ordering = ('-created',)


# Comment Model
class blogComment(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


# Like Model
LIKE_CHOICES = {
    ('Read','Read'),
    ('Unread','Unread'),
}

class blogRead(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    value = models.CharField(max_length=10,choices=LIKE_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}--{self.blog}--{self.value}"
    
