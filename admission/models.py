from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import *
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Angkatan(models.Model):
    tahun = models.CharField(max_length=4)
    semester = models.CharField(max_length=10)
    deskripsi = models.CharField(max_length=255)

    def __str__(self):
        return self.tahun


class Admission(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=100)
    asal_sekolah = models.CharField(max_length=30)
    tempat_lahir = models.CharField(max_length=35)
    tanggal_lahir = models.DateField()

    DITERIMA = 'Diterima'
    TDKDITERIMA = 'Tidak Diterima'
    PENDING = 'Pending'

    CHOICES = (
        (DITERIMA, DITERIMA),
        (PENDING, PENDING),
        (TDKDITERIMA, TDKDITERIMA),
    )
    status = models.CharField(
        max_length=255, choices=CHOICES, default=PENDING)
    angkatan_id = models.ForeignKey(
        Angkatan, on_delete=models.RESTRICT, null=True)
    pengguna = models.ForeignKey(
        User, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.nama
