from django.contrib import admin
from .models import *


@admin.register(MKB)
class MKBAdmin(admin.ModelAdmin):
    search_fields = ['code', 'diagnosis']

    pass

@admin.register(KSG)
class KSGAdmin(admin.ModelAdmin):
    list_filter = ['st_type', 'profile']
    search_fields = ['code', 'name']
    pass



admin.site.register(Scheme)
admin.site.register(Profile)
admin.site.register(Result)
admin.site.register(Department)
