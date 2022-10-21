import imp
from article.models import Kategori
from rest_framework import serializers

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'nama', 'deskripsi']