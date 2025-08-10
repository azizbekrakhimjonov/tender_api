from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profil
from .serializers import ProfilSerializer

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})

@api_view(['GET'])
def get_items(request):
    employees = Profil.objects.all()
    serializer = ProfilSerializer(employees, many=True)
    return Response({'data': serializer.data})

@api_view(["POST"])
def register_user(request):
    serializer = ProfilSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Successfully registered"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_items(request, pk):
    try:
        employee = Profil.objects.get(pk=pk)
    except Profil.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    employee.delete()
    return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)