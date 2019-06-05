from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Employees(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=256, blank=False, null=True)
    location = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    birth_date = models.DateField(null=True, blank=True)
    yearly_salary = models.DecimalField(max_digits=50, decimal_places=2)
    role = models.TextField()
    degree = models.CharField(max_length=256)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('employee:index')

    def __str__(self):
        return self.name