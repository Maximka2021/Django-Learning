from rest_framework.serializers import ModelSerializer
from .models import Address
from .models import Games

class AddressSerializer(ModelSerializer):
    class Meta:
        model=Address
        fields = '__all__'

class GamesSerializer(ModelSerializer):
    class Meta:
        model=Games
        fields = '__all__'
