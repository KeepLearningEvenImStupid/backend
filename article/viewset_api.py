from article.models import Kategori, Artikel
from article.serializers import KategoriSerializer, ArtikelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import *
from rest_framework import filters
from user import serializers
from .models import *
from django_filters.rest_framework import DjangoFilterBackend


class KategoriViewSetAdmin(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nama']

    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class ArtikelViewSetAdmin(viewsets.ModelViewSet):
    queryset = Artikel.objects.all()
    serializer_class = ArtikelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

    def perform_create(self, serializer, **kwargs):
        serializer.save(creator=self.request.user)


class ArtikelViewAll(generics.ListAPIView):
    serializer_class = ArtikelSerializer
    queryset = Artikel.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['kategori_slug']


class ArtikelDetail(generics.ListAPIView):
    serializer_class = ArtikelSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        kategori = self.kwargs['kategori_slug']
        artikel = self.kwargs['artikel_slug']
        return Artikel.objects.filter(kategori_slug=kategori, artikel_slug=artikel)


class ArtikelKategoriDetail(generics.ListAPIView):
    serializer_class = ArtikelSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        kategori = self.kwargs['kategori_slug']
        return Artikel.objects.filter(kategori_slug=kategori)


class KategoriDetail(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = KategoriSerializer
    queryset = Kategori.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug']
