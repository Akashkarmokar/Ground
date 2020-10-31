from django.contrib import admin
from .models import Domain,Solution,solutionLike


# Register your models here.
admin.site.register(Domain)
admin.site.register(Solution)
admin.site.register(solutionLike)