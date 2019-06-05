
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "employee"

# need to do 
# create employee
# delete employee
# modify employee
# add comments (notes) to employees
# fire employees

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='index'),
    path('add/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('view/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_update'),
]