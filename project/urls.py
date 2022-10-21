<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from article.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('kategori/', KategoriViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
=======
from knox import views as knox_views
from admission.views import studentRegisterView
from user.views import *
from user import views
from django.contrib import admin
from django.urls import path, include
from admission.views import AdmissionViewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'Admission', AdmissionViewset)


urlpatterns = [
    path('', include(router.urls)),
>>>>>>> 22c15a7f7ac92f141800385b54da0307ba75ce18
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('User-Register/', userRegisterAPI.as_view(), name='register-user'),
    path('Student-Register/', studentRegisterView.as_view(), name='register-user'),
    path('login-gate/', userLogin.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('Token/', views.tokenViewSet.as_view()),

]
