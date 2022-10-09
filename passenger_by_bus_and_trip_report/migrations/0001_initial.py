# Generated by Django 3.2.9 on 2022-10-09 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index_translation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='passenger_by_bus_and_trip_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp1', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('device_location1', models.CharField(blank=True, default='', max_length=50, verbose_name='ID e Matrícula do Autocarro')),
                ('route_reg_no1', models.IntegerField(blank=True, default='', verbose_name='Direcção do Autocarro')),
                ('route_reg_no', models.IntegerField(blank=True, default='', verbose_name='Direcção do Autocarro')),
                ('customer_profile_name', models.CharField(blank=True, default='', max_length=50, verbose_name='Perfil do passageiro')),
                ('card_uid3', models.CharField(blank=True, default='', max_length=50, verbose_name='Codigo do Cartão')),
                ('timestamp', models.TimeField(blank=True, default='', verbose_name='Hora de Entrada')),
                ('stationfrom_short_name', models.CharField(blank=True, default='', max_length=50, verbose_name='Entrada no Autocarro')),
                ('chout_timestamp', models.TimeField(blank=True, default='', verbose_name='Hora de Saida')),
                ('stationto_short_name', models.CharField(blank=True, default='', max_length=50, verbose_name='Saida no Autocarro')),
                ('money_value', models.DecimalField(blank=True, decimal_places=3, default='', max_digits=30, verbose_name='Valor Pago')),
                ('transaction_count', models.IntegerField(blank=True, default='', verbose_name='Nº de Transações Diárias')),
                ('money_value1', models.DecimalField(blank=True, decimal_places=3, default='', max_digits=30, verbose_name='Total do valor pago')),
                ('transaction_count2', models.IntegerField(blank=True, default='', verbose_name='Total de transações diárias')),
                ('money_value3', models.DecimalField(blank=True, decimal_places=3, default='', max_digits=30, verbose_name='Total de transações diárias')),
                ('bus_nr', models.IntegerField(blank=True, default='', verbose_name='Nº de Autocarro')),
                ('line_reg_no1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passengerRouta', to='index_translation.routa')),
                ('spz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passengerBus', to='index_translation.bus')),
            ],
        ),
    ]
