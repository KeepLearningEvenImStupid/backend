from django.shortcuts import render
from admission.models import Admission, AdmissionSerializer
from rest_framework import viewsets

# Create your views here.
class AdmissionViewset(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer