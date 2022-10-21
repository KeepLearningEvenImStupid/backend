from dataclasses import fields
from tkinter.tix import INTEGER
from admission.models import Admission
from rest_framework import serializers
from django.contrib.auth.models import Group


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = ['id', 'nama', 'alamat', 'asal_sekolah',
                  'tempat_lahir', 'tanggal_lahir', 'angkatan_id', 'pengguna', 'status']
