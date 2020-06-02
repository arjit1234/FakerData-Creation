from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    salary=models.IntegerField()
    job=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

