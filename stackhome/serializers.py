from rest_framework import serializers, fields
from stackhome.models import Apartment, Room, Rent
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    apartments = serializers.PrimaryKeyRelatedField(many=True, queryset=Apartment.objects.all())
    rooms = serializers.PrimaryKeyRelatedField(many=True, queryset=Room.objects.all())

    class Meta:
        model = get_user_model()
        fields = ['id', 'image', 'email', 'id_card', 'phone_number', 'full_name',
                  'active', 'staff', 'admin', 'created_at', 'last_login', 'apartments', 'rooms']
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            validated_data['email'],
            validated_data['id_card'],
            validated_data['phone_number'],
            validated_data['full_name'],
            validated_data['password'],
            validated_data['staff'],
            validated_data['admin'],
            validated_data['image'],
        )

        return user


class ApartmentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    features = fields.MultipleChoiceField(choices=Apartment.FEATURES, allow_blank=True)

    class Meta:
        model = Apartment
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'email', 'id_card', 'phone_number', 'full_name',
            'active', 'staff', 'admin', 'password', 'image',
        ]

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


class RoomSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    features = fields.MultipleChoiceField(choices=Room.FEATURES, allow_blank=True)

    class Meta:
        model = Room
        fields = '__all__'


class RentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rent
        fields = '__all__'


class ListRentSerializer(serializers.ModelSerializer):
    tenant = UserSerializer(many=False, read_only=True)
    apartment = ApartmentSerializer(many=False, read_only=True)
    room = RoomSerializer(many=False, read_only=True)

    class Meta:
        model = Rent
        fields = '__all__'
