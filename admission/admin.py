from django.contrib import admin
from .models import *
# Register your models here.


def refresh_objects(modeladmin, request, queryset):
    for object in queryset:
        object.save()


refresh_objects.short_description = "Update selected objects."


class SeleksiAdmin(admin.ModelAdmin):
    actions = [refresh_objects]


class AdmissionAdmin(admin.ModelAdmin):
    actions = [refresh_objects]


admin.site.register(Seleksi, SeleksiAdmin)
admin.site.register(Admission, AdmissionAdmin)
