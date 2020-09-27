from django.db import models

# Create your models here.
class Pastebindb(models.Model):
    user_name = models.CharField(max_length=70)
    poster_name = models.CharField(max_length=300,blank=False)
    poster = models.TextField()
    poster_type = models.CharField(max_length=10)
    poster_url = models.CharField(max_length=10,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)