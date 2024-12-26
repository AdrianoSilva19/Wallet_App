from django.db import models



# Create your models here.
class Wages(models.Model):
    company = models.CharField(max_length=100)
    year = models.IntegerField()
    month = models.CharField(max_length=20)
    wage = models.DecimalField(max_digits=10, decimal_places=2)
    

class HouseExpenses(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=20)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    general_expenses = models.DecimalField(max_digits=10, decimal_places=2)