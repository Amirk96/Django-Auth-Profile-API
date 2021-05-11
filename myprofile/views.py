from django.shortcuts import render
from rest_framework import generics
from myprofile.serializer import MyProfileSerializer
from myprofile.models import MyProfileModel

class MyProfileApi(generics.ListCreateAPIView):
    queryset = MyProfileModel.objects.all()
    serializer_class = MyProfileSerializer  