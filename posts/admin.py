from django.contrib import admin
from .models import Link,Post,Comment
# Register your models here.
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display=['id','address','addressname','user']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','post','date','postlink']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display= ['id','comment','post','user']

