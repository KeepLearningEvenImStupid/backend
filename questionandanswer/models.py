from email.policy import default
from statistics import mode
from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import User
from slugify import slugify


class pertanyaanDanJawabanModels(models.Model):
    penanya = models.CharField(max_length=255, blank=True)
    pertanyaan = models.TextField(blank=True)
    nama = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    no_hp = models.CharField(max_length=255, null=True, blank=True)
    judul_pertanyaan = models.CharField(max_length=255, blank=True)

    dibuat_pada = models.DateTimeField(auto_now_add=True, null=True)
    dijawab_pada = models.DateTimeField(auto_now=True, null=True)

    penjawab = models.CharField(max_length=255, blank=True)
    jawaban = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
