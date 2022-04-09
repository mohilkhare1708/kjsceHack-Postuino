from django.urls import path
from django.contrib.auth import views as auth_views
from mainapp import views

urlpatterns = [
    path('', views.home_page, name='home-page')
]
