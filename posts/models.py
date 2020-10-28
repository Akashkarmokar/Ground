from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils.safestring import mark_safe
from users.models import Profile
# Create your models here.

# Post model 
class Post(models.Model):
    heading = models.CharField(max_length=50)
    link = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='posts',validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank=True)
    liked = models.ManyToManyField(Profile,blank=True,related_name='likes')
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='posts')


    def __str__(self):
        return str(self.content[:20])

    def num_likes(self):
        return self.liked.all().count()


    def num_comments(self):
        return self.comment_set.all().count()

    # def post_photo(self):
    #     return mark_safe('<img src="{}" width="70"/>'.format(self.image.url))

    class Meta:
        ordering = ('-created',)



# Comment Model
class Comment(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


# Like Model
LIKE_CHOICES = {
    ('Like','Like'),
    ('Unlike','Unlike'),
}

class Like(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(max_length=10,choices=LIKE_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}--{self.post}--{self.value}"
    