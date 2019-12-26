from django.db import models
from med.models import *
from geo.models import Locality

class Patient(models.Model):
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        #ordering = ('name', )

    name = models.CharField(
        max_length=300,
        verbose_name = 'ФИО',

    )

    birhtdate = models.DateField(
        verbose_name = 'Дата рождения'
    )

    locality =  models.ForeignKey(
        Locality,
        verbose_name='Место жительства',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name
