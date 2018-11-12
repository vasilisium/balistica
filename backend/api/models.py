from django.db import models

# Create your models here.

class Person(models.Model):
    '''Персона'''
    last_name = models.CharField('Прізвище', max_length=30)
    first_name = models.CharField('Ім\'я', max_length=30)
    second_name = models.CharField('По батькові', max_length=30)
    address = models.TextField('Адреса') 
    mobile = models.CharField('Номер мобільного', max_length=13)
    date_created = models.DateTimeField('Дата/час зпису', auto_now_add=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name[0:1:]}.{self.second_name[0:1:]}.'

    class Meta:
        verbose_name = 'Особа - реєстраційні данні'
        verbose_name_plural = 'Особа - реєстраційні данні'

class Wepon(models.Model):
    '''Зброя'''
    owner = models.ForeignKey(Person, verbose_name="Власник", on_delete=models.DO_NOTHING, null=True)
    brend = models.CharField("Марка", max_length=30)
    model = models.CharField("Модель", max_length=30)
    calibre = models.CharField("Калібр", max_length=15)
    serial_number = models.CharField("Номер", max_length=30)
    date_created = models.DateTimeField('Дата/час зпису', auto_now_add=True)

    def __str__(self):
        return f'{self.brend} {self.model} {self.calibre} №{self.serial_number}'

    class Meta:
        verbose_name = 'Зброя'
        verbose_name_plural = 'Зброя - перелік'

class Ammo(models.Model):
    '''Тип набою'''
    description = models.CharField('Тип набою', max_length=30)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Тип набою'
        verbose_name_plural = 'Типи набоїв'

class Shooting(models.Model):
    ''' Модель записа відстрілу зброї'''
    person = models.ForeignKey(Person, verbose_name="Власник", on_delete = models.DO_NOTHING)
    wepon = models.ForeignKey(Wepon, verbose_name="Зброя", on_delete = models.DO_NOTHING, )
    ammo = models.ForeignKey(Ammo, verbose_name="Тип набоїв", on_delete = models.DO_NOTHING)
    date_Shooting = models.DateTimeField("дата/час", auto_now_add=True)
    document = models.CharField('Номер документа про оплату', max_length=20, default='')
    safe_number = models.CharField('Номер сейфу зберігання', max_length=5, default='')

    class Meta:
        verbose_name = 'Відстріл - запис відстрілу зброї'
        verbose_name_plural = 'Відстріл - записи відстрілу зброї'



