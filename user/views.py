from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serializers import *
from rest_framework import viewsets

# Create your views here.


class userDataViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer


class groupDataViewSets(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = groupSerializer
