from .models import Form
from .serializers import FormSerializer
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import *
# Create your views here.


class FormAdmin(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subject']

    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class FormUser(generics.CreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subject']
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
