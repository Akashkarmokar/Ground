from django.contrib import admin
from .models import Blog,blogComment,blogRead,Category


class BlogAdmin(admin.ModelAdmin):

    list_display = ('content' , 'author')
    list_per_page = 5
    list_max_show_all = 50

class blogCommentadmin(admin.ModelAdmin):
    
    list_display = ('user' , 'blog' , 'body' , 'updated')
    list_per_page = 10
    list_max_show_all = 100
    
class blogReadadmin(admin.ModelAdmin):
    list_display = ('user' , 'blog', 'value')


# Register your models here.
admin.site.register(Blog,BlogAdmin)
admin.site.register(blogComment,blogCommentadmin)
admin.site.register(blogRead,blogReadadmin)
admin.site.register(Category)