from django.shortcuts import render
from admission.models import Admission
from rest_framework import viewsets
from .serializer import AdmissionSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class AdmissionViewset(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    permission_classes = [IsAuthenticated]
