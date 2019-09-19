from rest_framework import serializers
from stackhome.models import Apartment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    apartments = serializers.PrimaryKeyRelatedField(many=True, queryset=Apartment.objects.all())

    class Meta:
        model = User
        # fields = ['id', 'username', 'apartments']
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Apartment
        fields = ['owner', 'address', 'equipped', 'bedrooms', 'living_room', 'bathroom',
                  'price', 'features', 'description', 'available', 'created']
