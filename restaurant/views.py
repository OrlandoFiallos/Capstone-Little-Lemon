from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Booking, Menu
from .serializers import MenuSerializer, UserSerializer, BookingSerializer
from rest_framework.authentication import TokenAuthentication

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]