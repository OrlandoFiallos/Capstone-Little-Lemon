from django.contrib.auth.models import User 
from .models import Menu, Booking
from rest_framework import serializers 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','is_superuser','is_active']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu 
        fields = ['id','title','price']