# Generated by Django 3.2.9 on 2022-03-16 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CSVS', '0004_auto_20220309_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Capacity summary report', 'Capacity summary report'), ('Conductor Sales Report', 'Conductor Sales Report'), ('Corridor performance report', 'Corridor performance report'), ('Passenger by bus and trip report', 'Passenger by bus and trip report'), ('Settlement file operator', 'Settlement file operator'), ('Cooperarive', 'Cooperarive'), ('Corridor', 'Corridor'), ('Routa', 'Routa'), ('Assign', 'Assign'), ('Manager', 'Manager'), ('Bus', 'Bus')], default='', max_length=50, null=True, verbose_name='Nome do Ficheiro')),
                ('file_name', models.FileField(upload_to='static/csvs', verbose_name='Ficheiro')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
                ('file_row', models.IntegerField(blank=True, null=True, verbose_name='Nº de Linhas')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Nome')),
                ('phone', models.CharField(max_length=200, null=True, verbose_name='Nº de Telefone')),
                ('emails', models.CharField(max_length=200, null=True, verbose_name='Email')),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]