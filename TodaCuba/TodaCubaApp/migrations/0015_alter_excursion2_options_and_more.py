# Generated by Django 4.2.1 on 2023-06-08 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodaCubaApp', '0014_alter_excursion1_informacion_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='excursion2',
            options={},
        ),
        migrations.AlterField(
            model_name='excursion2',
            name='Informacion',
            field=models.CharField(max_length=2000),
        ),
        migrations.AddConstraint(
            model_name='excursion2',
            constraint=models.UniqueConstraint(fields=('id',), name='unique_excursion2'),
        ),
    ]
