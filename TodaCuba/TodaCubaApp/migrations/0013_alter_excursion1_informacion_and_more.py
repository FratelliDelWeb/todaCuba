# Generated by Django 4.2.1 on 2023-06-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodaCubaApp', '0012_excursion2_excursion3_excursion4_excursion5_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion1',
            name='Informacion',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='excursion2',
            name='Informacion',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='excursion3',
            name='Informacion',
            field=models.CharField(max_length=3000),
        ),
    ]
