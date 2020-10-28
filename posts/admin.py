from django.contrib import admin
from .models import Post,Comment,Like


class Postadmin(admin.ModelAdmin):

    list_display = ('content' , 'image')
    list_per_page = 5
    list_max_show_all = 50

class Commentadmin(admin.ModelAdmin):
    
    list_display = ('user' , 'post' , 'body' , 'updated')
    list_per_page = 10
    list_max_show_all = 100
    
class Likeadmin(admin.ModelAdmin):
    
    list_display = ('user' , 'post', 'value')


# Register your models here.
admin.site.register(Post,Postadmin)
admin.site.register(Comment,Commentadmin)
admin.site.register(Like,Likeadmin)