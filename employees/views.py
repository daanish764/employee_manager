from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Employees
from . import forms 
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, "employee/index.html")

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employees

    # we should only be getting the employees that we are managing.
    def get_queryset(self):
        return Employees.objects.filter(manager=self.request.user)

    login_url = '/'
    redirect_field_name = ''

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employees
    form_class = forms.EmployeeCreateForm

    def form_valid(self, form):
        employee = form.save(commit=False)
        employee.manager = self.request.user
        employee.save()  # This is redundant, see comments.
        return super(EmployeeCreateView, self).form_valid(form)


    login_url = '/'
    redirect_field_name = ''

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employees

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employees
    fields = ('name', 'location', 'gender', 'birth_date', 'yearly_salary', 'role', 'degree', 'description')

    def get_success_url(self):
        return reverse('employee:employee_detail', kwargs={'pk': self.object.id})

    login_url = '/'
    redirect_field_name = ''
