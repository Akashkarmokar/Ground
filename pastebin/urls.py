from django.urls import path
from .import views

app_name = 'pastebin'

urlpatterns = [
    path('bin/',views.bin,name='bin_url'),
    path('show/',views.show,name='show_url'),
    path('bin/delete/<int:id>/',views.delete,name='delete_url'),
    path('bin/update/<int:up_id>/',views.update_post,name='update_url'),
    path('sharedCode/<str:rand_url>/',views.show,name='sharedCode'),
]
