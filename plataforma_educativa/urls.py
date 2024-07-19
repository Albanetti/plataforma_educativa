from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_academica/', include('gestion_academica.urls')),
    path('', include('gestion_academica.urls')), 
]
