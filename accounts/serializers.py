from rest_framework import serializers
from .models import FreightOrder
from .models import Profil

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ['username', 'email', 'password']

class FreightOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreightOrder
        fields = "__all__"
