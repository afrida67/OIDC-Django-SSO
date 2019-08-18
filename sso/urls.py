from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ssoapp.urls')),
    path('oidc/', include('mozilla_django_oidc.urls')),
]
