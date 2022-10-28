from article.models import Kategori, Artikel
from article.serializers import KategoriSerializer, ArtikelSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nama']
    

class ArtikelViewSet(viewsets.ModelViewSet):
    queryset = Artikel.objects.all()
    serializer_class = ArtikelSerializer