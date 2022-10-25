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


router = routers.DefaultRouter()
router.register('kategori', KategoriViewSet)
router.register('Admission', AdmissionViewset)
router.register('Angkatan', AngkatanViewset)
router.register('article', ArtikelViewSet)
router.register('pertanyaan', pertanyaanViewsets)
router.register('jawaban', jawabanViewsets)

urlpatterns = [

    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('User-Register/', userRegisterAPI.as_view(), name='register-user'),
    path('Student-Register/', studentRegisterView.as_view(), name='register-user'),
    path('login-gate/', userLogin.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('Token/', views.tokenViewSet.as_view()),


]
