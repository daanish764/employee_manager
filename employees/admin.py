from django.contrib import admin

# Register your models here.
from .models import Employees
from .models import Notes

admin.site.register(Employees)
admin.site.register(Notes)