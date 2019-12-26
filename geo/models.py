from django.db import models

class Municipality(models.Model):

    class Meta:
        verbose_name = 'Муниципальное образование'
        verbose_name_plural = 'Муниципальные образования'
        ordering = ('name', )

    name = models.CharField(
        max_length=200,
        verbose_name='Муниципальное образование'
    )

    def __str__(self):
        return self.name


class Locality(models.Model):

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'
        ordering = ('name',)

    name = models.CharField(
        verbose_name='Населенный пункт',
        max_length=200
    )

    municipality = models.ForeignKey(
        Municipality,
        verbose_name='Муниципальное образование',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def get_municipality(self):
        return self.municiality

    def __str__(self):
        return self.name
