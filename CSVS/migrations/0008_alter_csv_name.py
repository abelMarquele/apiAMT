# Generated by Django 3.2.9 on 2022-02-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSVS', '0007_alter_csv_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='name',
            field=models.CharField(blank=True, choices=[('Capacity summary report', 'Capacity summary report'), ('Conductor Sales Report', 'Conductor Sales Report'), ('Corridor performance report', 'Corridor performance report'), ('Passenger by bus and trip report', 'Passenger by bus and trip report'), ('Settlement file operator', 'Settlement file operator'), ('Cooperarive', 'Cooperarive'), ('Corridor', 'Corridor'), ('Routa', 'Routa'), ('Assign', 'Assign'), ('Manager', 'Manager'), ('Bus', 'Bus')], default='', max_length=50, null=True, verbose_name='Nome do Ficheiro'),
        ),
    ]
