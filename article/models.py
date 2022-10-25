from asyncio.windows_events import NULL
from django.db import models
from slugify import slugify


class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()
    slug = models.SlugField(max_length=255, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = slugify(self.nama)

    def save(self, force_insert=False, force_update=False, *args, **kwargs) -> None:

        if self.slug is not NULL:
            pass
        elif self.slug is NULL:
            self.slug = slugify(self.nama)

        return super().save(force_insert, force_update, *args, **kwargs)


class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    konten = models.TextField()
    thumbnail = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    kategori = models.ForeignKey(
        Kategori, on_delete=models.RESTRICT)
    kategori_slug = models.CharField(max_length=255, null=True)
    artikel_slug = models.CharField(max_length=255, null=True)
    kategori_value = models.CharField(max_length=255, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kategori_value = self.kategori.nama
        self.kategori_slug = slugify(self.kategori.nama)
        self.artikel_slug = slugify(self.judul)

    def save(self, force_insert=False, force_update=False, *args, **kwargs) -> None:

        if self.article_slug is not NULL:
            pass
        elif self.article_slug is NULL:
            self.article_slug = self.judul
        return super().save(force_insert, force_update, *args, **kwargs)
