from django.shortcuts import render
from admission.models import Admission
from rest_framework import viewsets
from .serializer import AdmissionSerializer
# Create your views here.


class AdmissionViewset(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
