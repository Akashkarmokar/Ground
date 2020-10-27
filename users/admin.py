from django.contrib import admin
from .models import Profile,Relationship

# Register your models here.

class Porfileadmin(admin.ModelAdmin):

    list_display = ('first_name' , 'last_name' , 'user' , 'bio' ,'profile_photo')
    list_filter = ['user','first_name']
    list_per_page = 5
    list_max_show_all = 50
    
admin.site.register(Profile,Porfileadmin)
admin.site.register(Relationship)
