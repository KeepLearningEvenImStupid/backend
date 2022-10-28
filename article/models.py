from asyncio.windows_events import NULL
from typing_extensions import Required
from django.db import models
from slugify import slugify
from django.urls import reverse


class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()
    slug = models.CharField(max_length=255, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = slugify(self.nama)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.nama)
        return super().save(*args, **kwargs)


class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    konten = models.TextField()
    thumbnail = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    kategori_value = models.CharField(max_length=255, blank=True, null=True)
    kategori_slug = models.SlugField(max_length=255, blank=True, null=True)
    artikel_slug = models.SlugField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs) -> None:
        self.kategori_value = self.kategori.nama
        self.kategori_slug = slugify(self.kategori_value)
        self.artikel_slug = slugify(self.judul)
        return super().save(*args, **kwargs)
