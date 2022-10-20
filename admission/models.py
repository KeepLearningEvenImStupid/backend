from ast import And
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import *
from django.utils.translation import gettext_lazy as _
from django.db.models import Case, When, F
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

    __original_status = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_status = self.status

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.status != self.__original_status:
            if self.status == "Diterima":
                group = Group.objects.get(name='Mahasiswa')
                group.user_set.add(self.pengguna)
            if self.status == "Tidak Diterima":
                group = Group.objects.get(name='Mahasiswa')
                group.user_set.remove(self.pengguna)
        else:
            pass
        super().save(force_insert, force_update, *args, **kwargs)
        self.__original_status = self.status
