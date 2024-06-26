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
            name='conductor_sales_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField(blank=True, default='', verbose_name='Nº Cooperativa')),
                ('company_name', models.CharField(blank=True, default='', max_length=50, verbose_name='Cooperativa')),
                ('device', models.CharField(blank=True, default='', max_length=50, verbose_name='Nº do Dispositivo')),
                ('conductor_id', models.IntegerField(blank=True, default='', verbose_name='ID do Gestor')),
                ('conductor_last_name', models.CharField(blank=True, default='', max_length=50, verbose_name='Gestor')),
                ('number', models.IntegerField(blank=True, default='', verbose_name='Total de passageiros')),
                ('amount', models.DecimalField(blank=True, decimal_places=3, default='', max_digits=30, verbose_name='Receita da Cooperativa')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('conductor_first_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conductorBus', to='index_translation.bus')),
            ],
        ),
    ]
