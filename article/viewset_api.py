from article.models import Kategori, Artikel
from article.serializers import KategoriSerializer, ArtikelSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import *
from rest_framework import filters
from user import serializers
from .models import *
from django_filters.rest_framework import DjangoFilterBackend


class KategoriViewSetAdmin(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class ArtikelViewSetAdmin(viewsets.ModelViewSet):
    queryset = Artikel.objects.all()
    serializer_class = ArtikelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class ArtikelViewAll(generics.ListAPIView):
    serializer_class = ArtikelSerializer
    queryset = Artikel.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['kategori_slug']


class ArtikelKategoriDetail(generics.ListAPIView):
    serializer_class = ArtikelSerializer

    def get_queryset(self, **kwargs):

        kategori = self.kwargs['kategori_slug']
        return Artikel.objects.filter(kategori_slug=kategori)


class KategoriDetail(generics.ListAPIView):
    serializer_class = KategoriSerializer
    queryset = Kategori.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug']
