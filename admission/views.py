from django.shortcuts import render
from admission.models import Admission, Angkatan
from rest_framework import viewsets, generics
from .serializer import AdmissionSerializer, mahasiswaRegisterSerializer
from .serializer import AngkatanSerializer, mahasiswaRegisterSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.


class AdmissionViewset(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    permission_classes = [IsAuthenticated]

class AngkatanViewset(viewsets.ModelViewSet):
    queryset = Angkatan.objects.all()
    serializer_class = AngkatanSerializer
    permission_classes = [IsAuthenticated]


class mahasiswaRegisterAPI(generics.GenericAPIView):
    serializer_class = mahasiswaRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": mahasiswaRegisterSerializer(user, context=self.get_serializer_context()).data,
        })
