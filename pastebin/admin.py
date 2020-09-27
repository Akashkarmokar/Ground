from django.contrib import admin
from pastebin.models import Pastebindb

# Register your models here.
@admin.register(Pastebindb)
class Paste_bin_db_admin(admin.ModelAdmin):
    list_display = ['id','user_name','poster_name','poster','poster_type','poster_url','timestamp']