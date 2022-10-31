from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import pertanyaanDanJawabanModels
from .serializers import *
from rest_framework.permissions import *
from rest_framework import filters

# Create your views here.


class PertanyaanView(generics.ListCreateAPIView):
    queryset = pertanyaanDanJawabanModels.objects.all()
    serializer_class = PertanyaanSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer, **kwargs):
        serializer.save(penanya=self.request.user)


class JawabanEdit(viewsets.ModelViewSet):
    serializer_class = JawabanSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    queryset = pertanyaanDanJawabanModels.objects.all()

    def perform_create(self, serializer, **kwargs):
        serializer.save(penjawab=self.request.user)


class JawabanViewAll(generics.ListAPIView):
    serializer_class = JawabanSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    queryset = pertanyaanDanJawabanModels.objects.all()


class PertanyaanJawabanViewAll(generics.ListAPIView):
    serializer_class = PertanyaanJawabanSerializer
    queryset = pertanyaanDanJawabanModels.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['pertanyaan', 'jawaban']


class PertanyaanJawabanFilter(generics.ListAPIView):
    serializer_class = PertanyaanJawabanSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        slug = self.kwargs['slug']
        return pertanyaanDanJawabanModels.objects.filter(slug=slug)


class PertanyaanJawabanDetail(generics.ListAPIView):
    serializer_class = PertanyaanJawabanSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        slug = self.kwargs['slug']
        penanya = self.kwargs['penanya']
        return pertanyaanDanJawabanModels.objects.filter(slug=slug, penanya=penanya)
