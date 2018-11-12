from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer


from .serializers import PersonSerializer, WeponSerializer, ShootingSerializer, AmmoSerializer
from .models import Person, Wepon, Shooting, Ammo


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PersonView(APIView):

    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons)
        return Response(serializer.data)
