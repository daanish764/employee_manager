from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Employees, Notes
from . import forms 
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

    login_url = '/'
    redirect_field_name = ''


    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        notes = Notes.objects.filter(employee_id=self.object.pk)       
        context['notes'] = notes
        return context

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employees
    fields = ('name', 'location', 'gender', 'birth_date', 'yearly_salary', 'role', 'degree', 'description')

    def get_success_url(self):
        return reverse('employee:employee_detail', kwargs={'pk': self.object.id})

    login_url = '/'
    redirect_field_name = ''

class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employees

    success_url = reverse_lazy('employee:index')

    login_url = '/'
    redirect_field_name = ''


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes

    success_url = reverse_lazy('employee:index')

    login_url = '/'
    redirect_field_name = ''

@login_required
def add_note_to_post(request, pk):

    employee = get_object_or_404(Employees, pk=pk)
    
    if request.method == 'POST':
        form = forms.NoteCreateForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            employee = get_object_or_404(Employees, pk=pk)
            note.employee = employee
            note.save()
            return redirect('employee:employee_detail', pk=pk)
            pass
    else:
        form = forms.NoteCreateForm()

    return render(request, 'employees/notes_form.html', {'form':form, 'employees':employee})