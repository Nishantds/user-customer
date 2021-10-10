from django.shortcuts import render
from rest_framework.response import Response
from.models import Customer
from.serializers import CustomerSerializers
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class CustomerViewSet(viewsets.ViewSet):
    def create(self,request):
            serializer=CustomerSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   