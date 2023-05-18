from django.contrib import admin
from django.urls import path
from django.urls import include

# Rutas para la aplicación
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('generator.urls')),
]
