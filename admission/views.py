from django.shortcuts import render
from admission.models import Admission
from rest_framework import viewsets, generics
from .serializer import AdmissionSerializer
from django.contrib.auth.models import Group
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class AdmissionViewset(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

    pengguna_field_name = 'pengguna'
    pengguna_obj = Admission.objects.first()
    pengguna_field_object = Admission._meta.get_field(pengguna_field_name)
    pengguna_field_value = getattr(pengguna_obj, pengguna_field_object.attname)

    status_field_name = 'status'
    status_obj = Admission.objects.first()
    status_field_object = Admission._meta.get_field(status_field_name)
    status_field_value = getattr(status_obj, status_field_object.attname)

    if status_field_name == 'Diterima':
        group = Group.objects.get(name='Mahasiswa')
        group.user_set.add(pengguna_field_value)

    elif status_field_name == 'Tidak Diterima':
        g = Group.objects.get(name='Mahasiswa')
        g.user_set.remove(pengguna_field_name)

    else:
        pass
