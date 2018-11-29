from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    )
from .models import (
    Person, 
    Wepon, 
    Shooting,
    Ammo
    )
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField, EmailField

def dateToStr(date, format="%d.%m.%Y %H:%M:%S"):
    return date.strftime(format)

User = get_user_model()
class UserLoginSerializer(ModelSerializer):
    token = CharField(blank=True, editable=False)
    username = CharField(blank=True)
    email = EmailField(blank=True)

    class Meta:
        model = User
        fields = (
            'username', 
            'email',
            'password',
            'token',
        )
        extra_kwargs = {'password':
            {'write_only': True}
        }


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'first_name',
            'second_name',
            'last_name',
            'address',
            'mobile',
            'date_created'
        )

class PersonNameSerializer(ModelSerializer):
    date_created = SerializerMethodField()
    def get_date_created(self, obj):
        return dateToStr(obj.date_created)

    class Meta:
        model = Person
        fields = (
            'id',
            'first_name',
            'second_name',
            'last_name',
            'date_created',
        )


class WeponSerializer(ModelSerializer):
    owner = PersonNameSerializer()

    date_created = SerializerMethodField()
    def get_date_created(self, obj):
        return dateToStr(obj.date_created)

    class Meta:
        model = Wepon
        fields =(
            'id',
            'owner',
            'brand',
            'model',
            'calibre',
            'serial_number',
            'date_created'
        )


class AmmoSerializer(ModelSerializer):
    class Meta:
        model = Ammo
        fields = ('id', 'description',)

class ShootingSerializer(ModelSerializer):

    wepon  = WeponSerializer()

    ammo = AmmoSerializer()

    date_Shooting = SerializerMethodField()
    def get_date_Shooting(self, obj):
        return dateToStr(obj.date_Shooting)

    class Meta:
        model = Shooting
        # ordering = ['date_Shooting']
        # order_by = ['-date_Shooting']
        fields = (
            'id',
            'wepon', 
            'date_Shooting', 
            'ammo', 
            'document', 
            'safe_number',
        )

    
