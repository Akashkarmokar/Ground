from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=70,blank=False)
    email = models.EmailField(max_length=200,blank=False)
    mobileNo = models.CharField(max_length=20,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)

    class Meta:
        ordering = ('-created',)