from django.contrib import admin
from django.urls import path, include
from admission.views import AdmissionViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('admission/', AdmissionViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
