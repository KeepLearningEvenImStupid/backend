from django.contrib import admin
from django.urls import path, include, re_path
from article.viewset_api import *
from rest_framework import routers
from knox import views as knox_views
from admission.views import studentRegisterView
from questionanswer.views import jawabanViewsets, pertanyaanViewsets
from user.views import *
from user import views
from django.contrib import admin
from django.urls import path, include
from admission.views import AdmissionViewset
from admission.views import AngkatanViewset
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register('Angkatan', AngkatanViewset)
router.register('pertanyaan', pertanyaanViewsets)
router.register('jawaban', jawabanViewsets)

urlpatterns = [

    # URL untuk django Swagger
    path('',  schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('api/api-iblam.json',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # URL untuk masuk ke page django admin
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),

    # URL untuk artikel,kategori yang diperuntukan untuk user
    path('artikel/', ArtikelDetail.as_view()),
    path('kategori/', KategoriDetail.as_view()),

    # URL untuk keperluan admin(Full akses HTTP Method)
    path('admission/', AdmissionViewset.as_view()),
    path('kategori-admin/', KategoriViewSet.as_view()),
    path('artikel-admin/', ArtikelViewSet.as_view()),

    # URL untuk keperluan register user dan pendaftaran mahasiswa
    path('user-register/', userRegisterAPI.as_view(), name='register-user'),
    path('student-register/', studentRegisterView.as_view(),
         name='register-student'),

    # URL untuk keperluan login user
    path('login-gate/', userLogin.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('Token/', views.tokenViewSet.as_view()),

]
