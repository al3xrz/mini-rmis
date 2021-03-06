# Generated by Django 2.2 on 2019-12-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0002_scheme_ksg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименоваие')),
            ],
            options={
                'verbose_name': 'Исход заболевания',
                'verbose_name_plural': 'Исход заболевания',
            },
        ),
        migrations.AlterField(
            model_name='mkb',
            name='ksg',
            field=models.ManyToManyField(to='med.KSG', verbose_name='КСГ'),
        ),
    ]
