from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.pagination import PageNumberPagination

from .serializers import (
    PersonSerializer, 
    WeponSerializer, 
    AmmoSerializer,
    ShootingSerializer,
    UserLoginSerializer,
    )
from .models import (
    Person,
    Wepon,
    Shooting,
    Ammo,
    )

from django.contrib.auth import get_user_model
User = get_user_model()


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    # queryset = User.objects.all()

    def post(self, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        

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

class ShootingView(ListAPIView):
    queryset = Shooting.objects.all()
    serializer_class = ShootingSerializer
    # permission_classes = [IsAuthenticated,]