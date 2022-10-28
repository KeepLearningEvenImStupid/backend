from django.contrib import admin
from .models import *
# Register your models here.


def refresh_objects(modeladmin, request, queryset):
    for object in queryset:
        object.save()


refresh_objects.short_description = "Update selected objects."


class KategoriAdmin(admin.ModelAdmin):
    actions = [refresh_objects]


class ArticleAdmin(admin.ModelAdmin):
    actions = [refresh_objects]


admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Artikel, ArticleAdmin)
