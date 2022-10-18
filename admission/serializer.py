from dataclasses import fields
from admission.models import Admission
from rest_framework import serializers
from django.contrib.auth.models import Group


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = ['id', 'nama', 'alamat', 'asal_sekolah',
                  'tempat_lahir', 'tanggal_lahir', 'angkatan_id', 'pengguna']


class mahasiswaRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = ('nama', 'alamat', 'asal_sekolah',
                  'tempat_lahir', 'tanggal_lahir')

    def create(self, validated_data):
        mahasiswa = Admission.objects.create(
            validated_data['nama'], validated_data['alamat'], validated_data['asal_sekolah'], validated_data['tempat_lahir'], validated_data['tanggal_lahir'])
        user = Admission.pengguna
        group = Group.objects.get(name='Mahasiswa')
        group.user_set.add(user)
        return mahasiswa
