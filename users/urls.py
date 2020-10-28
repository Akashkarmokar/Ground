from django.urls import path
from .import views

app_name = 'users'

urlpatterns =[
    path('profile/<profileId>/',views.profile,name='profile'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
]