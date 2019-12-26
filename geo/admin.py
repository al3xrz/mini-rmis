from django.contrib import admin

from .models import *

admin.site.site_header = 'Администрирование'


# Register your models here.

admin.site.register(Municipality)
admin.site.register(Locality)
