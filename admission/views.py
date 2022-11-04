from admission.models import Admission, Angkatan, Seleksi
from rest_framework import viewsets, generics
from .serializer import *
from rest_framework import viewsets, filters
from rest_framework.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class AdmissionViewset(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id', 'nama', 'alamat',
                     'asal_sekolah', 'tempat_lahir', 'tanggal_lahir']


class studentRegisterView(generics.CreateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer, **kwargs):
        serializer.save(pengguna=self.request.user)


class studentChooseStudyProgramAPI(generics.CreateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionProgramStudiSerializer
    permission_classes = [IsAuthenticated]


class AngkatanViewset(viewsets.ModelViewSet):
    queryset = Angkatan.objects.all()
    serializer_class = AngkatanSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    search_fields = ['id', 'tahun', 'semester', 'deskripsi']


class jalurSeleksiAdminAPI(generics.ListAPIView):
    queryset = Seleksi.objects.all()
    serializer_class = JalurSeleksiSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class jalurSeleksiUserAPI(generics.ListAPIView):
    queryset = Seleksi.objects.all()
    serializer_class = JalurSeleksiSerializer
    permission_classes = [AllowAny]


class jalurSeleksiDetailUserAPI(generics.ListAPIView):
    serializer_class = JalurSeleksiDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Seleksi.objects.filter(slug=slug)
