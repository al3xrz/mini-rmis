from django.urls import path
from django.urls import include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)



urlpatterns = [
    path('', main_entry_point, name = 'main_entry_point'),
    path('api/', include(router.urls)),
    #path('patients/<int:id>', patient, name = 'patient'),
]
