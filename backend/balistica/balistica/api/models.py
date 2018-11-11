from django.db import models

# Create your models here.

# class Person(models.Model):
#     '''Персона'''
#     first_name = models.CharField()
#     second_name = models.CharField()
#     last_name = models.CharField()
#     address = models.CharField() 
#     mobile = models.CharField()
#     date = models.DateTimeField('Дата/час зпису', auto_now_add=True)

# class Wepon(models.Model):
#     '''Зброя'''
#     brend = models.CharField("Марка")
#     model = models.CharField("Модель")
#     calibre = models.DecimalField("Калібр", decimal_places=2)
#     serial_number = models.CharField("Номер")
#     date = models.DateTimeField('Дата/час зпису', auto_now_add=True)

# class Ammo(models.Model):
#     '''Тип набою'''
#     description = models.CharField('Тип набою')

# class Shooting(models.Model):
#     ''' Модель записа відстрілу зброї'''
#     person = models.ForeignKey(Person, verbose_name="Власник", on_delete = models.DO_NOTHING)
#     wepon = models.ForeignKey(Wepon, verbose_name="Зброя", on_delete = models.DO_NOTHING)
#     ammo = models.ForeignKey(Ammo, verbose_name="Тип набоїв", on_delete = models.DO_NOTHING)
#     date = models.DateTimeField("дата/час", auto_now_add=True)



