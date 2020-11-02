from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = 'users'

urlpatterns =[
    path('profile/<profileId>/',views.profile,name='profile'),
    path('signup/',views.signup,name='signup'),
    # path('signup/',views.SignupView.as_view(),name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('changepass',views.changepass,name='changepass'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),

    # path('reset_password/',
    #     auth_views.PasswordResetView.as_view(),
    #     name="reset_password"),

    # path('reset_password_sent/',
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done"),

    # path('reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm"),

    # path('reset_password_complete/',
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete"),
]