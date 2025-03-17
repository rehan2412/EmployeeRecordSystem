from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.FloatField()
    date_of_joining = models.DateField()
