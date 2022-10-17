from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user import views
from user.views import *

router = routers.DefaultRouter()
router.register(r'UserData', views.userDataViewSets)
router.register(r'GroupData', views.groupDataViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('register/', RegisterAPI.as_view(), name='register'),
]
