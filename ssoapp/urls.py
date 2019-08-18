from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
]