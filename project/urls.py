from knox import views as knox_views
from user.views import *
from user import views
from django.contrib import admin
from django.urls import path, include
from admission.views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('Admission', AdmissionViewset)
router.register('Angkatan', AngkatanViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('User-Register/', userRegisterAPI.as_view(), name='register-user'),
    path('Admission-Register/', mahasiswaRegisterAPI.as_view(),
         name='register-admission'),
    path('Angkatan/', mahasiswaRegisterAPI.as_view(),
         name='Angkatan'),
    path('login-gate/', userLogin.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('Token/', views.tokenViewSet.as_view()),

]
