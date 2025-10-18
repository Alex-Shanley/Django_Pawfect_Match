from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('pets/', include('pets.urls')),
    path('contact/', include('contact.urls')),
    path('auth/', include('auth_app.urls')),  
    path('accounts/', include('django.contrib.auth.urls')), 

        path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='auth_app/password_reset_done.html'), 
        name='password_reset_done'
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
