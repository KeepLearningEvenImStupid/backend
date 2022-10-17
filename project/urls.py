from knox import views as knox_views
from user.views import *
from user import views
from django.contrib import admin
from django.urls import path, include
from admission.views import AdmissionViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('admission/', AdmissionViewset)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('User-Register/', userRegisterAPI.as_view(), name='register'),
    path('Dosen-Register/', dosenRegisterAPI.as_view(), name='register'),
    path('Admin-Register/', adminRegisterAPI.as_view(), name='register'),
    path('login-gate/', userLogin.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('Token/', views.tokenViewSet.as_view()),

]
