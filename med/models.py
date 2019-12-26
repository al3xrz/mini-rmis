from django.db import models


class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    code = models.IntegerField(
            verbose_name='Код',
    )

    name = models.CharField(
        max_length=50,
        verbose_name='Наименование',
    )

    def __str__(self):
        return self.name




st_CHOICES = (
        ( 'Круглосуточный' , 'Круглосуточный'),
        ( 'Дневной', 'Дневной'),
    )








class KSG(models.Model):

    class Meta:
        verbose_name = 'КСГ'
        verbose_name_plural = 'КСГ'
        ordering = ('code', )

    st_type = models.CharField(
        choices=st_CHOICES,
        max_length=10,
        verbose_name='Тип стационара',
    )

    code = models.CharField(
        max_length=20,
        verbose_name='Код'
    )

    name = models.CharField(
        max_length=200,
        verbose_name='Наименоваие КСГ'
    )

    kz = models.FloatField(
        verbose_name='КЗ'
    )

    profile = models.ForeignKey(
        Profile,
        verbose_name='Профиль',
        on_delete=models.SET_NULL,
        null=True,

    )

    def __str__(self):
            return '[%s стационар] [%s]     %s'%(self.st_type, self.code, self.name)







class Scheme(models.Model):
    class Meta:
        verbose_name = 'Схема лекарственной терапии'
        verbose_name_plural = 'Схемы лекарственной терапии'

    st_type = models.CharField(
        choices=st_CHOICES,
        max_length=10,
        verbose_name='Тип стационара',
    )

    code = models.CharField(
        max_length=20,
        verbose_name='Код'
    )

    mnn = models.CharField(
        max_length=200,
        verbose_name='МНН лекарственных препаратов'
    )

    name = models.CharField(
        max_length=200,
        verbose_name='Наименование и описание схемы'
    )

    col = models.CharField(
        max_length=200,
        verbose_name='Количество дней в тарифе'
    )

    ksg = models.ForeignKey(
        KSG,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name = 'КСГ',
    )

    sign = models.CharField(
        max_length=50,
        verbose_name='Признак не ЖНВЛП'
    )

    comments = models.TextField(
        verbose_name='Примечание'
    )

    def __str__(self):
        return self.name









class MKB(models.Model):
    class Meta:
        verbose_name = 'МКБ 10'
        verbose_name_plural = 'МКБ 10'
        ordering = ('code', )

    code = models.CharField(
        max_length=200,
        verbose_name='Код'
    )

    diagnosis  = models.CharField(
        max_length=50,
        verbose_name='Диагноз'
    )

    ksg = models.ManyToManyField(
        KSG,
    )

    def get_datestates(self):
        return KSG.objects.filter(mkb=self)


    def __str__(self):
        return '[%s] %s'%(self.code, self.diagnosis);
