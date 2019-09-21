from rest_framework import serializers
from stackhome.models import Apartment
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    apartments = serializers.PrimaryKeyRelatedField(many=True, queryset=Apartment.objects.all())

    class Meta:
        model = get_user_model()
        # fields = ['id', 'username', 'apartments']
        fields = '__all__'

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            validated_data['email'],
            validated_data['id_card'],
            validated_data['phone_number'],
            validated_data['full_name'],
            validated_data['password'],
            validated_data['staff'],
            validated_data['admin'],
        )

        return user


class ApartmentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Apartment
        fields = ['owner', 'address', 'equipped', 'bedrooms', 'living_room', 'bathroom',
                  'price', 'features', 'description', 'available', 'created']
