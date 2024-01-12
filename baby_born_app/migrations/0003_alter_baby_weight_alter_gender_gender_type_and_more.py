# Generated by Django 5.0.1 on 2024-01-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby_born_app', '0002_carousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='weight',
            field=models.FloatField(verbose_name='Agramy'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='gender_type',
            field=models.CharField(max_length=10, verbose_name='Jyns ady'),
        ),
        migrations.AlterField(
            model_name='smen',
            name='time_part',
            field=models.CharField(max_length=50, verbose_name='Işleýän wagty'),
        ),
    ]
