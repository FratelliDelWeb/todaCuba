# Generated by Django 4.2.1 on 2023-06-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodaCubaApp', '0010_excursion1_nombredelaexcursion'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion1',
            name='descripcionDeLaExcursion',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
