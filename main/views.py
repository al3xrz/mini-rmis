from django.shortcuts import render
from django.http import HttpResponse
from main.models import *

# Create your views here.

def main_entry_point(request):
    patients = Patient.objects.all()
    return render(request, 'main_table.html', { 'patients' : patients })
