from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.auth_.urls')),  # Altere 'auth_' para 'apps.auth_'
    path('', include('django.contrib.auth.urls')),
]
