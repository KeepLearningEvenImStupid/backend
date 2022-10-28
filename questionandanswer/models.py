from email.policy import default
from statistics import mode
from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import User
from slugify import slugify


class pertanyaanDanJawabanModels(models.Model):
    penanya_obj = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name='penanya')
    penanya = models.CharField(max_length=255, blank=True)
    pertanyaan = models.CharField(max_length=255, blank=True)

    penjawab_obj = models.ForeignKey(User, on_delete=models.RESTRICT)
    penjawab = models.CharField(max_length=255, blank=True)
    jawaban = models.CharField(max_length=255, blank=True)

    slug = models.SlugField(max_length=255, default="Belum Diisi")

    def __init__(self, *args, **kwargs):
        self.penanya = self.penanya_obj.username
        self.penjawab = self.penjawab_obj.username
        self.slug = slugify(self.pertanyaan)
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs) -> None:
        self.penanya = self.penanya_obj.username
        self.penjawab = self.penjawab_obj.username
        self.slug = slugify(self.pertanyaan)
        return super().save(*args, **kwargs)
