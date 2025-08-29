from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profil,  FreightOrder
from .serializers import  ProfilSerializer, FreightOrderSerializer


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
    return Response({"message": "Consumer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)






# 🔹 GET (list) va POST (create)
@api_view(['GET', 'POST'])
def freight_order_list(request):
    if request.method == 'GET':
        orders = FreightOrder.objects.all()
        serializer = FreightOrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FreightOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 🔹 GET (detail), PUT (update), DELETE (remove)
@api_view(['GET', 'PUT', 'DELETE'])
def freight_order_detail(request, pk):
    try:
        order = FreightOrder.objects.get(pk=pk)
    except FreightOrder.DoesNotExist:
        return Response({'error': 'Freight Order not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FreightOrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FreightOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
