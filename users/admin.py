from django.contrib import admin
from .models import Profile,Relationship

# Register your models here.
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['first_name','last_name','user','bio','email','country','avater','friends','slug','updated','created']
admin.site.register(Profile)
admin.site.register(Relationship)
