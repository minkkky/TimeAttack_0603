from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

class Drink(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    info = models.CharField(max_length=100)
    allergy_info = models.CharField(max_length=100)