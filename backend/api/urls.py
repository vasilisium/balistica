from django.urls import path
from .views import (
    PersonView, PersonUpdateView,
    WeponView,
    AmmoView,
    ShootingView,

    UserLoginView,
    )

urlpatterns = [
    path('person/', PersonView.as_view()),
    path('person/edit/<id>', PersonUpdateView.as_view()),
    path('wepon/', WeponView.as_view()),
    path('ammo/', AmmoView.as_view()),
    path('shooting/', ShootingView.as_view()),
    path('login/', UserLoginView.as_view(), name='login'),
]