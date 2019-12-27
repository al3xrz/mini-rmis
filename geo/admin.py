from django.contrib import admin
from .models import *

admin.site.site_header = 'Администрирование'


# Register your models here.

@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    search_fields = ['name']
    pass


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_filter = ['municipality']
    search_fields = ['name']
