from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Person, Wepon, Shooting, Ammo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name') 

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'second_name', 'last_name', 'address', 'mobile')

class WeponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wepon
        fields =('brend', 'model', 'calibre', 'serial_number')

class ShootingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shooting
        fields = ('person', 'wepon', 'date', 'ammo')

class AmmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ammo
        fields = ('description')

