from unicodedata import name
from django.shortcuts import render
from admission.models import Admission, Angkatan
from rest_framework import viewsets, generics
from .serializer import AdmissionSerializer
from .serializer import AngkatanSerializer
from django.contrib.auth.models import Group
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import status, permissions
from rest_framework.permissions import *
from django.views.generic.edit import CreateView
# Create your views here.


class AdmissionViewset(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class studentRegisterView(generics.CreateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer


class AngkatanViewset(viewsets.ModelViewSet):
    queryset = Angkatan.objects.all()
    serializer_class = AngkatanSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class studentRegisterView(generics.CreateAPIView):
    queryset = Angkatan.objects.all()
    serializer_class = AngkatanSerializer