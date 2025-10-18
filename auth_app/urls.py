from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  

app_name = 'auth_app'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('signup/', views.register_view, name='signup'),
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='auth_app/forgot_password.html'), name='forgot_password'),
     
     path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='auth_app/password_reset_done.html'), 
        name='password_reset_done'
    ),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='auth_app/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth_app/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]