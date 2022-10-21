from django.contrib import admin
from django.urls import path, include
from article.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('kategori/', KategoriViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
