from rest_framework import serializers
from stackhome.models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        img = serializers.IntegerField(default=10)
        fields = ['address', 'equipped', 'bedrooms', 'living_room', 'bathroom',
                  'price', 'features', 'description', 'available', 'created']
