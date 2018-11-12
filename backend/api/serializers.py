from rest_framework.serializers import (
    ModelSerializer,
    # HyperlinkedModelSerializer,
    SerializerMethodField,
    )
from .models import (
    Person, 
    # Wepon, 
    Shooting,
    Ammo
    )

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'second_name', 'last_name', 'address', 'mobile', 'date_created')

# class WeponSerializer(ModelSerializer):
#     class Meta:
#         model = Wepon
#         fields =('brend', 'model', 'calibre', 'serial_number', 'date_created')

class AmmoSerializer(ModelSerializer):
    class Meta:
        model = Ammo
        fields = ('description',)

class ShootingSerializer(ModelSerializer):
    class Meta:
        model = Shooting

        # person  = SerializerMethodField()

        fields = (
            'person',
            # 'wepon', 
            'date_Shooting', 
            'ammo', 
            'document', 
            'safe_number'
            )

        # def get_person(self, obj):
        #     return str(obj.person.last_name)
