# Generated by Django 4.2.1 on 2023-06-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodaCubaApp', '0020_alter_casas_options_alter_casas_provincia'),
    ]

    operations = [
        migrations.AddField(
            model_name='casas',
            name='nombreCasa',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
