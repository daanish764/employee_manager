
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "employee"

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='index'),
    path('add/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('view/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('add_note/<int:pk>/', views.add_note_to_post, name='add_note_to_employee'),
    path('delete_note/<int:pk>/', views.NoteDeleteView.as_view() ,name='delete_note')
]