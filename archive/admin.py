from django.contrib import admin
from .models import Domain,Solution,solutionLike


# Register your models here.
class solutionAdmin(admin.ModelAdmin):
    
    list_display = ('domain' , 'number' , 'link')
    list_per_page = 5
    
admin.site.register(Domain)
admin.site.register(Solution,solutionAdmin)
admin.site.register(solutionLike)