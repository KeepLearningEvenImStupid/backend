from django.db import models

# Create your models here.


class visitorModels(models.Model):
    id_anggota = models.CharField(max_length=255)
    institusi = models.CharField(max_length=255)


class anggotaModels(models.Model):
    id_anggota = models.AutoField(primary_key=True)
    password = models.CharField(max_length=255)
