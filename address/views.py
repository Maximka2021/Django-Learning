from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Address
from .models import Games
from .serializer import AddressSerializer
from .serializer import GamesSerializer

class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class GamesViewSet(ModelViewSet):
    serializer_class = GamesSerializer
    queryset = Games.objects.all()


