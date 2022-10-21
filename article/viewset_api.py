from article.models import Kategori, Artikel
from article.serializers import KategoriSerializer, ArtikelSerializer
from rest_framework import viewsets

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class ArtikelViewSet(viewsets.ModelViewSet):
    queryset = Artikel.objects.all()
    serializer_class = ArtikelSerializer