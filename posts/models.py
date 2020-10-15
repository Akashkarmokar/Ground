from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#Links model 
class Link(models.Model):
    address = models.CharField(max_length=100)
    addressname = models.CharField(max_length=80)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.address
    

#Posts model 
class Post(models.Model):
    content = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now=True)
    postlink = models.ForeignKey(Link,on_delete=models.CASCADE,related_name="problem")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.postlink 

#comments model
class Comment(models.Model):
    body = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    