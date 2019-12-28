from django.db import models
from med.models import *
from geo.models import Locality

st_CHOICES = (
        ( 'Круглосуточный' , 'Круглосуточный'),
        ( 'Дневной', 'Дневной'),
)


class Treatment(models.Model):
    class Meta:
        verbose_name = 'Лечение'
        verbose_name_plural = 'Лечение'


    st_type = models.CharField(
        choices=st_CHOICES,
        max_length=20,
        verbose_name='Тип стационара',

    )

    date_in = models.DateField(
        verbose_name = "Дата поступления"
    )

    date_out = models.DateField(
        verbose_name = "Дата выписки",
        blank = True,
        null = True,
    )


    department = models.ForeignKey(
        Department,
        on_delete = models.SET_NULL,
        verbose_name = 'Отделение',
        null = True
    )

    mkb = models.ForeignKey(
        MKB,
        on_delete = models.SET_NULL,
        verbose_name = 'Диагноз (МКБ 10)',
        null = True,
        blank = True,
    )

    scheme = models.ForeignKey(
        Scheme,
        on_delete = models.SET_NULL,
        verbose_name = 'Лекарственные препараты',
        null = True,
        blank = True,
    )

    result = models.ForeignKey(
        Result,
        on_delete = models.SET_NULL,
        verbose_name = 'Исход заболевания',
        null = True,
        blank = True,
    )

    def __str__(self):
        return "%s - %s"%(self.date_in, self.department)




class Patient(models.Model):
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        #ordering = ('name', )

    name = models.CharField(
        max_length=300,
        verbose_name = 'ФИО',

    )

    birthdate = models.DateField(
        verbose_name = 'Дата рождения'
    )

    locality =  models.ForeignKey(
        Locality,
        verbose_name='Место жительства',
        on_delete=models.SET_NULL,
        null=True,
    )

    treatment = models.ForeignKey(
        Treatment,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name
