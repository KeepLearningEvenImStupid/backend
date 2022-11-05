from knox.views import LoginView as KnoxLoginView
from .serializer import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
# Create your views here.


class RegisterAnggotaAPI(generics.GenericAPIView):
    serializer_class = AnggotaRegisterSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        anggota = serializer.save()
        return Response({
            "anggota": AnggotaForAdminSerializer(anggota, context=self.get_serializer_context()).data,
        })


class anggotaLoginAPI(KnoxLoginView):
    permission_classes = [AllowAny]
    redirect_authenticated_user = True

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        anggota = serializer.validated_data['id_anggota']
        login(request, anggota)
        return super(anggotaLoginAPI, self).post(request, format=None)
