from article.models import Kategori, Artikel
from article.serializers import KategoriSerializer, ArtikelSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import *
from rest_framework import filters


class KategoriViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class ArtikelViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artikel.objects.all()
    serializer_class = ArtikelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class ArtikelDetail(generics.ListAPIView):
    serializer_class = ArtikelSerializer
    queryset = Artikel.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['judul', 'konten', 'kategori__nama']
    permission_classes = [AllowAny]


class KategoriDetail(generics.ListAPIView):
    serializer_class = ArtikelSerializer
    queryset = Artikel.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['judul', 'konten', 'kategori__nama']
    permission_classes = [AllowAny]
