from rest_framework import generics
from stackhome.models import Apartment, Room
from stackhome.serializers import ApartmentSerializer, UserSerializer, UserRegisterSerializer, RoomSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from stackhome.permissions import IsOwnerOrReadOnly, IsTheUserOrReadOnly, IsStaff


class ApartmentList(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class ApartmentAdd(generics.CreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaff]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ApartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListCreateAPIView):  # Change it with a simple CreateAPIView
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserRegister(generics.CreateAPIView):  # Change it with a simple CreateAPIView
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsTheUserOrReadOnly]


class MyApartments(generics.ListAPIView):
    serializer_class = ApartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Apartment.objects.filter(owner=user)


# Rooms ______________________
class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class RoomAdd(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaff]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MyRooms(generics.ListAPIView):
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Room.objects.filter(owner=user)
