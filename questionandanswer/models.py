from email.policy import default
from statistics import mode
from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import User
from slugify import slugify


class pertanyaanDanJawabanModels(models.Model):
    penanya = models.CharField(max_length=255, blank=True)
    pertanyaan = models.CharField(max_length=255, blank=True)
    penjawab = models.CharField(max_length=255, blank=True)
    jawaban = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255)
