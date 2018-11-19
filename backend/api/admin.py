from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import (
    Person, 
    Wepon,
    WeponType,
    Ammo,
    Shooting,
)

class RefererFilter(admin.SimpleListFilter):
    title = 'наявністю власника'
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'owner__isnull'

    def lookups(self, request, model_admin):
        return (
            ('False', 'Має власника'),
            ('True', 'Не має власника'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'False':
            return queryset.filter(owner__isnull=False)
        if self.value() == 'True':
            return queryset.filter(owner__isnull=True)


class PersonsAdmin(admin.ModelAdmin):
    '''Записи власників зброї'''
    list_display = (
        'last_name',
        'first_name',
        'second_name',
        'address',
        'mobile',
        'date_created'
    )

class WeponAdmin(admin.ModelAdmin):
    '''Перелік зброї'''
    list_display = (
        'owner',
        'brand',
        'model',
        'calibre',
        'serial_number',
        'date_created',
    )
    list_filter =  (RefererFilter,) 

class WponTypeAdmin(admin.ModelAdmin):
    '''Перелік типів зброї'''
    list_display = (
        'description',
        'description_plural'
        )

class AmmoAdmin(admin.ModelAdmin):
    '''Перелік набоїв зброї'''
    list_display = ('description',)

class ShootingAdmin(admin.ModelAdmin):
    '''Відстріл зброї'''
    list_display = (
        'wepon', 
        'date_Shooting', 
        'ammo', 
        'document', 
        'safe_number'
    )

admin.site.register(Person, PersonsAdmin)
admin.site.register(Wepon, WeponAdmin)
admin.site.register(WeponType, WponTypeAdmin)
admin.site.register(Ammo, AmmoAdmin)
admin.site.register(Shooting, ShootingAdmin)