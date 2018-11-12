from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.pagination import PageNumberPagination

from .serializers import (
    PersonSerializer, 
    WeponSerializer, 
    AmmoSerializer,
    ShootingSerializer,
    )
from .models import (
    Person,
    Wepon,
    Shooting,
    Ammo,
    )


class PersonView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated,]

class WeponView(ListAPIView):
    queryset = Wepon.objects.all()
    serializer_class = WeponSerializer
    permission_classes = [IsAuthenticated,]

class AmmoView(ListAPIView):
    queryset = Ammo.objects.all()
    serializer_class = AmmoSerializer
    permission_classes = [IsAuthenticated,]
