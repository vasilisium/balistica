from django.urls import path
from .views import (
    PersonView, 
    WeponView,
    AmmoView,
    )

urlpatterns = [
    path('persons/', PersonView.as_view()),
    path('wepons/', WeponView.as_view()),
    path('ammo/', AmmoView.as_view()),
]