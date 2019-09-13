from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from stackhome.models import Apartment
from stackhome.serializers import ApartmentSerializer


@api_view(['GET', 'POST'])
def apartment_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        apartment = Apartment.objects.all()
        serializer = ApartmentSerializer(apartment, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def apartment_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        apartment = Apartment.objects.get(pk=pk)
    except Apartment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApartmentSerializer(apartment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApartmentSerializer(apartment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        apartment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)