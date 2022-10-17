from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user import views
from user.views import *
from knox import views as knox_views

router = routers.DefaultRouter()
router.register(r'UserData', views.userDataViewSets)
router.register(r'GroupData', views.groupDataViewSets)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('User-Register/', userRegisterAPI.as_view(), name='register'),
    path('Dosen-Register/', dosenRegisterAPI.as_view(), name='register'),
    path('Admin-Register/', adminRegisterAPI.as_view(), name='register'),
    path('login-gate/', userLogin.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('Token/', views.tokenViewSet.as_view()),
]
