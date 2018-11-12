from django.contrib import admin

from .models import (
    Person, 
    # Wepon,
    Ammo,
    Shooting,
)


class PersonsAdmin(admin.ModelAdmin):
    '''Записи власників зброї'''
    list_display = ('last_name', 'first_name', 'second_name',  'address', 'mobile', 'date_created')

# class WeponAdmin(admin.ModelAdmin):
#     '''Перелік зброї'''
#     list_display = ('brend', 'model', 'calibre', 'serial_number', 'date_created')

class AmmoAdmin(admin.ModelAdmin):
    '''Перелік набоїв зброї'''
    list_display = ('description',)

class ShootingAdmin(admin.ModelAdmin):
    '''Відстріл зброї'''
    list_display = ('person',
            # 'wepon', 
            'date_Shooting', 
            'ammo', 
            'document', 
            'safe_number')

admin.site.register(Person, PersonsAdmin)
# admin.site.register(Wepon, WeponAdmin)
admin.site.register(Ammo, AmmoAdmin)
admin.site.register(Shooting, ShootingAdmin)