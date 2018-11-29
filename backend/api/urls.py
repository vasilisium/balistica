from django.urls import path
from .views import (
    PersonView, 
    WeponView,
    AmmoView,
    ShootingView,

    UserLoginView,
    )

urlpatterns = [
    path('persons/', PersonView.as_view()),
    path('wepons/', WeponView.as_view()),
    path('ammo/', AmmoView.as_view()),
    path('shooting/', ShootingView.as_view()),
    path('login/', UserLoginView.as_view(), name='login'),
]