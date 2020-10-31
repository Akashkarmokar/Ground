from django.db import models
from users.models import Profile
# Create your models here.
class Feedback(models.Model):
    content = models.TextField(max_length=300,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.content[:20])

    class Meta:
        ordering = ('-created',)