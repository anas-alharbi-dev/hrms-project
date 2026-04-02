from django.db import models
from django.contrib.auth.models import User
from departments.models import Department


class Employee(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    job_title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
