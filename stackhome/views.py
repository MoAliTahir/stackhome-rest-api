from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from stackhome.models import Apartment
from stackhome.serializers import ApartmentSerializer


class ApartmentList(APIView):

    def get(self, request, format=None):
        """
        List all code snippets, or create a new snippet.
        """
        apartment = Apartment.objects.all()
        serializer = ApartmentSerializer(apartment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApartmentDetail(APIView):
    """
            Retrieve, update or delete a code snippet.
            """
    def get_object(self, request, pk):
        try:
            return Apartment.objects.get(pk=pk)
        except Apartment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = ApartmentSerializer(self.get_object(request, pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        apartment = self.get_object(request, pk)
        serializer = ApartmentSerializer(apartment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        apartment = self.get_object(request, pk)
        apartment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)