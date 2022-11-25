from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id   = models.AutoField
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile   = models.CharField(max_length=15)
    position = models.CharField(max_length=60)