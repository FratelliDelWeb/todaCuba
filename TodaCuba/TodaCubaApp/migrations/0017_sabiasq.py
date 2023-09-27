# Generated by Django 4.2.1 on 2023-06-08 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodaCubaApp', '0016_alter_excursion2_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SabiasQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDelArticulo', models.CharField(max_length=100)),
                ('descripcionDelArticulo', models.CharField(max_length=100)),
                ('leerMas', models.CharField(max_length=1000)),
                ('imagen1', models.ImageField(blank=True, null=True, upload_to='Imagenes')),
            ],
            options={
                'verbose_name': 'SabiasQs',
                'verbose_name_plural': 'SabiasQs',
            },
        ),
    ]
