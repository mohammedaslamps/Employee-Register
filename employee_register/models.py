from turtle import position
from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullName =models.CharField(max_length=100)
    emp_num = models.CharField(max_length=3)
    mobile =models.CharField(max_length=15)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)

    