from article.models import Kategori
from article.serializers import KategoriSerializer
from rest_framework import viewsets

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer