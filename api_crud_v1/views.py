from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api_crud_v1.models import Product
from api_crud_v1.serializers import ProductModelSerializer


@api_view(['GET'])
@parser_classes([JSONParser])
def products_list(request):
    products = Product.objects.all()
    if not products.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductModelSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def products_detail(request, pk: int):
    products = Product.objects.filter(id=pk)
    if not products.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductModelSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@parser_classes([JSONParser])
def products_create(request):
    serializer = ProductModelSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
@parser_classes([JSONParser])
def products_update(request, pk: int):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductModelSerializer(product, data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@parser_classes([JSONParser])
def products_delete(request, pk: int):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
