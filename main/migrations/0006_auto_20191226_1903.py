# Generated by Django 2.2 on 2019-12-26 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191226_1712'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ksg',
            options={'ordering': ('code',), 'verbose_name': 'КСГ', 'verbose_name_plural': 'КСГ'},
        ),
        migrations.AlterModelOptions(
            name='mkb',
            options={'ordering': ('code',), 'verbose_name': 'МКБ 10', 'verbose_name_plural': 'МКБ 10'},
        ),
        migrations.AddField(
            model_name='mkb',
            name='ksg',
            field=models.ManyToManyField(to='main.KSG'),
        ),
    ]
