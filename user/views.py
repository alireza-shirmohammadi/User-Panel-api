from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import ImageSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser

from rest_framework.decorators import parser_classes
from .models import Image,Manage
from rest_framework.views import APIView
# Create your views here.
'''
@api_view(['POST'])
@parser_classes([MultiPartParser])
@parser_classes([FormParser])
def ImageApi(request):
    ser=ImageSerializer(data=request.data['file'])
    if ser.Is_valid():
        ser.save()
        return Response(ser.data,status=status.HTTP_201_CREATED)
    else:
        return Response(Login_info.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class ImageApi(APIView):


    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
