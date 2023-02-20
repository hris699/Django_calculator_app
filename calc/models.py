from django.db import models

# Create your models here.
class Calculation(models.Model):
    operation=models.CharField(max_length=50)
    result=models.CharField(max_length=50)

class Memory(models.Model):
    number=models.CharField(max_length=50)
