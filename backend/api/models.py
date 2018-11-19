from django.db.models import Model
from django.db.models import (
    ForeignKey,
    CharField,
    TextField,
    DateTimeField,

)
from django.db.models import (
    DO_NOTHING,
    CASCADE,
)

# Create your models here.

class Person(Model):
    '''Персона'''
    last_name = CharField('Прізвище', max_length=30)
    first_name = CharField('Ім\'я', max_length=30)
    second_name = CharField('По батькові', max_length=30)
    address = TextField('Адреса') 
    mobile = CharField('Номер мобільного', max_length=13)
    date_created = DateTimeField('Дата/час зпису', auto_now_add=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name[0:1:]}.{self.second_name[0:1:]}.'

    class Meta:
        verbose_name = 'Особа - реєстраційні данні'
        verbose_name_plural = 'Особа - реєстраційні данні'


class Wepon(Model):
    '''Зброя'''
    # wepon_type = ForeignKey (WeponType, verbose_name="Тип зброї", on_delete=CASCADE)
    owner = ForeignKey(Person, verbose_name="Власник", on_delete=CASCADE)
    brand = CharField("Марка", max_length=30)
    model = CharField("Модель", max_length=30)
    calibre = CharField("Калібр", max_length=15)
    serial_number = CharField("Номер", max_length=30)
    date_created = DateTimeField('Дата/час зпису', auto_now_add=True)

    def __str__(self):
        return f'{self.brend} {self.model} {self.calibre} №{self.serial_number}'

    class Meta:
        verbose_name = 'Зброя'
        verbose_name_plural = 'Зброя - перелік'


class WeponType(Model):
    '''Тип зброї'''
    description = CharField('Тип зброї', max_length=30)
    description_plural = CharField('Тип зброї (множина)', max_length=30, default='asd' ) 

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Тип зброї'
        verbose_name_plural = 'Типи зброї'


class Ammo(Model):
    '''Тип набою'''
    description = CharField('Тип набою', max_length=30)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Тип набою'
        verbose_name_plural = 'Типи набоїв'


class Shooting(Model):
    ''' Модель записа відстрілу зброї'''
    wepon = ForeignKey(Wepon, verbose_name="Зброя", on_delete = CASCADE)
    ammo = ForeignKey(Ammo, verbose_name="Тип набоїв", on_delete = CASCADE)
    date_Shooting = DateTimeField("дата/час", auto_now_add=True)
    document = CharField('Номер документа про оплату', max_length=20, default='')
    safe_number = CharField('Номер сейфу зберігання', max_length=5, default='')

    class Meta:
        verbose_name = 'Відстріл - запис відстрілу зброї'
        verbose_name_plural = 'Відстріл - записи відстрілу зброї'



