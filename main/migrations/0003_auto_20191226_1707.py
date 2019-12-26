# Generated by Django 2.2 on 2019-12-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_mkb'),
    ]

    operations = [
        migrations.CreateModel(
            name='KSG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_type', models.CharField(choices=[('Круглосуточный', 'Круглосуточный'), ('Дневной', 'Дневной')], max_length=10, verbose_name='Тип стационара')),
                ('code', models.CharField(max_length=20, verbose_name='Код')),
                ('name', models.CharField(max_length=200, verbose_name='Наименоваие КСГ')),
                ('kz', models.FloatField(verbose_name='КЗ')),
                ('profile_code', models.IntegerField(verbose_name='Код профиля')),
                ('profile_name', models.CharField(max_length=200, verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Код МКБ',
                'verbose_name_plural': 'Код МКБ',
            },
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_type', models.CharField(choices=[('Круглосуточный', 'Круглосуточный'), ('Дневной', 'Дневной')], max_length=10, verbose_name='Тип стационара')),
                ('code', models.CharField(max_length=20, verbose_name='Код')),
                ('mnn', models.CharField(max_length=200, verbose_name='МНН лекарственных препаратов')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование и описание схемы')),
                ('col', models.CharField(max_length=200, verbose_name='Количество дней в тарифе')),
                ('sign', models.CharField(max_length=50, verbose_name='Признак не ЖНВЛП')),
                ('comments', models.CharField(max_length=400, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Схема лекарственной терапии',
                'verbose_name_plural': 'Схемы лекарственной терапии',
            },
        ),
        migrations.AlterField(
            model_name='mkb',
            name='code',
            field=models.CharField(max_length=200, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='mkb',
            name='diagnosis',
            field=models.CharField(max_length=50, verbose_name='Диагноз'),
        ),
    ]
