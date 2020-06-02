# Generated by Django 3.0.6 on 2020-06-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anestesia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=100)),
                ('dia_cirugia', models.CharField(max_length=10)),
                ('tipo_cirugiam', models.CharField(max_length=200)),
                ('cirujano', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
