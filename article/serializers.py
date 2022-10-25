from article.models import Kategori
from article.models import Artikel
from rest_framework import serializers


class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'nama', 'deskripsi', 'slug']


class ArtikelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artikel
        fields = ['id', 'judul', 'konten',
                  'thumbnail', 'creator', 'kategori']
