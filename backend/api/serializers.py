from rest_framework.serializers import (
    ModelSerializer,
    # HyperlinkedModelSerializer,
    SerializerMethodField,
    )
from .models import (
    Person, 
    Wepon, 
    Shooting,
    Ammo
    )

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'first_name',
            'second_name',
            'last_name',
            'address',
            'mobile',
            'date_created'
        )

class WeponSerializer(ModelSerializer):
    owner = SerializerMethodField()
    class Meta:
        model = Wepon
        fields =(
            'owner',
            'brend',
            'model',
            'calibre',
            'serial_number',
            'date_created'
        )

    def get_owner(self, obj):
        return str(obj.owner)


class AmmoSerializer(ModelSerializer):
    class Meta:
        model = Ammo
        fields = ('description',)

class ShootingSerializer(ModelSerializer):
    owner  = SerializerMethodField()
    def get_owner(self, obj):
        return str(obj.wepon.owner)

    wepon  = SerializerMethodField()
    def get_wepon(self, obj):
        return str(obj.wepon)

    ammo = SerializerMethodField()
    def get_ammo(self, obj):
        return str(obj.ammo)

    class Meta:
        model = Shooting
        fields = (
            'owner',
            'wepon', 
            'date_Shooting', 
            'ammo', 
            'document', 
            'safe_number',
        )

    
