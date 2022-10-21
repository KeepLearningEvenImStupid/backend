import imp
from article.models import Kategori
from article.models import Artikel
from rest_framework import serializers

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'nama', 'deskripsi']

class ArtikelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artikel
        fields = ['judul', 'konten', 'thumbnail', 'slug', 'creator', 'kategori']