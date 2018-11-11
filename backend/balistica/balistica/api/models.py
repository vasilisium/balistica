from django.db import models

# Create your models here.

class Person(models.Model):
    '''Модель Персона'''
    first_name = models.CharField(max=30)
    second_name = models.CharField(max=30)
    last_name = models.CharField(max=30)

    #TODO: заменить на ключ адреса
    address = models.CharField(max=100) 
    mobile = models.CharField(max=13)