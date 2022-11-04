from dataclasses import fields
from tkinter.tix import INTEGER
from admission.models import Admission, Angkatan, Seleksi
from rest_framework import serializers
from django.contrib.auth.models import Group


class AdmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admission
        fields = ['id', 'nama', 'alamat', 'asal_sekolah',
                  'tempat_lahir', 'tanggal_lahir', 'angkatan_id', 'pengguna', 'status']


class AdmissionProgramStudiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admission
        fields = ['program_studi']


class AngkatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Angkatan
        fields = ['id', 'tahun', 'semester', 'deskripsi']


class JalurSeleksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seleksi
        fields = ['kategori', 'deskripsi', 'awal_pendaftaran',
                  'akhir_pendaftaran', 'gelombang', 'formulir', 'periode_pendaftaran', 'sistem_kuliah']


class JalurSeleksiDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seleksi
        fields = ['kategori', 'deskripsi', 'awal_pendaftaran',
                  'akhir_pendaftaran', 'gelombang', 'periode_pendaftaran', 'sistem_kuliah', 'program_studi', 'strata', 'daya_tampung']
