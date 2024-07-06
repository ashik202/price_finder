from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import AccountSerializr
from . import models
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import MyTokenObtainPairSerializer, UrlSerializer
from rest_framework import generics
from .models import Account, Url
# Create your views here.


class RegisterUser(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializr

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class Urlview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

class UrlListview(APIView):
    def get(self,request,id):
        print('hello')
        data_obj = Url.objects.filter(user__pk = id)
        serializer_obj = UrlSerializer(data_obj,many = True)
        return Response(serializer_obj.data, status=status.HTTP_200_OK)
    
class UrlCreateview(APIView):
    def post(self,request):
        id = request.data['user']
        url_obj = Url.objects.filter(user__pk=id)
        print(url_obj)
        if len(url_obj)>= 3:
               data = {"message":"you can only add 3 url"}
               return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        




