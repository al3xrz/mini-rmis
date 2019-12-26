from django.contrib import admin

from .models import *

admin.site.site_header = 'Географическая информация'


# Register your models here.

admin.site.register(Municipality)
admin.site.register(Locality)
