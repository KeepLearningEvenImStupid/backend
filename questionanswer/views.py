from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import *
# Create your views here.


class pertanyaanViewsets(viewsets.ModelViewSet):
    queryset = pertanyaan.objects.all()
    serializer_class = pertanyaanSerializer
    permission_classes = [IsAuthenticated]


class jawabanViewsets(viewsets.ModelViewSet):
    queryset = jawabanModels.objects.all()
    serializer_class = jawabanSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
