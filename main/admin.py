from django.contrib import admin
from .models import *

admin.site.site_header = 'Администрирование'
admin.site.register(Patient)
admin.site.register(Treatment)
