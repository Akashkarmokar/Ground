from django.urls import path
from .import views

urlpatterns = [
    path('bin/',views.bin,name='bin_url'),
    path('show/',views.show,name='show_url'),
    path('bin/delete/<int:id>/',views.delete,name='delete_url'),
    path('bin/update/<int:up_id>/',views.update_post,name='update_url'),
]

#path('show/',views.show,name='show_url'),