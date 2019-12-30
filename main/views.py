from django.shortcuts import render
from django.http import HttpResponse
from main.models import *
from main.serializers import *
from rest_framework import viewsets


# Create your views here.

def main_entry_point(request):
    patients = Patient.objects.all()
    return render(request, 'main_table.html', { 'patients' : patients, })

def patient(request, id):
    patient = Patient.objects.get(id=id)
    print(patient)
    return render(request, 'patient.html', { 'patient' : patient ,})




class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
