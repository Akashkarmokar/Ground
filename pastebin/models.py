from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.
class Pastebindb(models.Model):
    poster_name = models.CharField(max_length=300,blank=False)
    poster = models.TextField()
    poster_type = models.CharField(max_length=10)
    poster_url = models.CharField(max_length=10,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='pastebin')

    class Meta:
        ordering = ('-timestamp',)