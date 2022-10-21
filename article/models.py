from django.db import models


class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama


class Artikel(models.Model):
    judul = models.CharField(max_length=120)
    konten = models.TextField()
    thumbnail = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    creator = models.CharField(max_length=255)
    kategori = models.ForeignKey(Kategori, on_delete=models.RESTRICT)

def __str__(self):
        return self.judul 

