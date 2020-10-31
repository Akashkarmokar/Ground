from django.urls import path
from .import views


app_name = "archive"

urlpatterns = [
    path('main/',views.main,name='main'),
]
