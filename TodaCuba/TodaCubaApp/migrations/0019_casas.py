# Generated by Django 4.2.1 on 2023-06-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodaCubaApp', '0018_alter_excursion2_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(max_length=50, null=True)),
                ('municipioLocacion', models.CharField(max_length=50, null=True)),
                ('Informacion', models.CharField(max_length=1000)),
                ('imagenPrincipal', models.ImageField(blank=True, null=True, upload_to='Imagenes')),
                ('imagen1', models.ImageField(blank=True, null=True, upload_to='Imagenes')),
                ('imagen2', models.ImageField(blank=True, null=True, upload_to='Imagenes')),
                ('imagen3', models.ImageField(blank=True, null=True, upload_to='Imagenes')),
                ('imagen4', models.ImageField(blank=True, null=True, upload_to='Imagenes')),
                ('imagen5', models.ImageField(blank=True, null=True, upload_to='Imagenes')),
                ('imagen6', models.ImageField(blank=True, null=True, upload_to='Imagenes')),
            ],
            options={
                'verbose_name': 'Casas',
                'verbose_name_plural': 'Casass',
            },
        ),
    ]
