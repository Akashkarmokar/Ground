from django.db import models
from users.models import Profile


# Create your models here.

class Domain(models.Model):
    name = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class Solution(models.Model):
    domain = models.ForeignKey(Domain,on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    like = models.ManyToManyField(Profile,blank=True,related_name='solution_like')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.domain} ----  {self.number}"

    # class Meta:
    #     ordering = ('like.all.count',)



LIKE_CHOICES = {
    ('Like','Like'),
    ('Unlike','Unlike'),
}

class solutionLike(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    solution = models.ForeignKey(Solution,on_delete=models.CASCADE)
    value = models.CharField(max_length=10,choices=LIKE_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}--{self.solution}--{self.value}"
    