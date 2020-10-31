"""Ground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home_url"),
    path('privecy/',views.privecy,name="privecy"),
    path('terms_condition/',views.terms_condition,name="terms_condition"),
    path('blog/',include('blog.urls',namespace='blog')),
    path('feedback/',views.feedback,name='feedback'),
    path('pastebin/',include('pastebin.urls',namespace='pastebin')),
    path('user/',include('users.urls',namespace='users')),
    path('posts/',include('posts.urls',namespace='posts')),
    
    

    path('search/',views.user_search,name='user_search'),


    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="users/passwordReset.html"),
        name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="users/passwordResetSent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="users/passwordResetForm.html"),
        name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="users/passwordResetDone.html"),
        name="password_reset_complete"),

    path('archive/',include('archive.urls',namespace='archive')),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.STATIC_ROOT)