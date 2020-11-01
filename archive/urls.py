from django.urls import path
from .import views


app_name = "archive"

urlpatterns = [
    path('main/',views.main_or_search,name='main_or_search'),
    path('delete_solution/<pk>/',views.delete_solution,name='delete_solution'),
]
