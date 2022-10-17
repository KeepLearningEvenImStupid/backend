from django.contrib import admin
from django.urls import path, include
from admission.views import AdmissionViewset
from rest_framework import routers
<<<<<<< HEAD
from user import views
from user.views import *
from knox import views as knox_views
=======
>>>>>>> a9af15421160d2d0c118cd5e7ea18c1e625893cf

router = routers.DefaultRouter()
router.register('admission/', AdmissionViewset)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('User-Register/', userRegisterAPI.as_view(), name='register'),
    path('Dosen-Register/', dosenRegisterAPI.as_view(), name='register'),
    path('Admin-Register/', adminRegisterAPI.as_view(), name='register'),
    path('login-gate/', userLogin.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('Token/', views.tokenViewSet.as_view()),
=======
>>>>>>> a9af15421160d2d0c118cd5e7ea18c1e625893cf
]
