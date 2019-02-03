from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=20)
    employment_date = models.DateField()
    salary = models.FloatField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank = True, null = True )