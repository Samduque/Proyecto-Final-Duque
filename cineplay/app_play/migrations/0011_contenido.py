# Generated by Django 5.1.1 on 2024-12-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_play', '0010_stream_portada_stream_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='contenido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('Pelicula', 'Pelicula'), ('Serie', 'Serie')], max_length=50)),
                ('puntuacion', models.FloatField(default=0.0)),
            ],
        ),
    ]