
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "auth_user"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_user, name="create"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
