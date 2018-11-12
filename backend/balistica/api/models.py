from django.db import models

# Create your models here.

class Person(models.Model):
    '''Персона'''
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100) 
    mobile = models.CharField(max_length=13)
    date = models.DateTimeField('Дата/час зпису', auto_now_add=True)

class Wepon(models.Model):
    '''Зброя'''
    brend = models.CharField("Марка", max_length=30)
    model = models.CharField("Модель", max_length=30)
    calibre = models.DecimalField("Калібр", decimal_places=2, max_digits=8)
    serial_number = models.CharField("Номер",max_length=30)
    date = models.DateTimeField('Дата/час зпису', auto_now_add=True)

class Ammo(models.Model):
    '''Тип набою'''
    description = models.CharField('Тип набою', max_length=30)

class Shooting(models.Model):
    ''' Модель записа відстрілу зброї'''
    person = models.ForeignKey(Person, verbose_name="Власник", on_delete = models.DO_NOTHING)
    wepon = models.ForeignKey(Wepon, verbose_name="Зброя", on_delete = models.DO_NOTHING)
    ammo = models.ForeignKey(Ammo, verbose_name="Тип набоїв", on_delete = models.DO_NOTHING)
    date = models.DateTimeField("дата/час", auto_now_add=True)



