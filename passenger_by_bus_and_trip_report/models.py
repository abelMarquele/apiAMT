from django.db import models

from index_translation.models import Routa

# Create your models here.



class passenger_by_bus_and_trip_report(models.Model):
    timestamp1 = models.DateField(verbose_name=('Data'),
                            blank=True,
                            null=True)
    device_location1 = models.CharField(verbose_name=('ID e Matrícula do Autocarro'),
                            default='',
                            blank=True)
    line_reg_no1 = models.ForeignKey(Routa, related_name="capacityRouta", on_delete=models.SET_NULL, null=True)
    route_reg_no1 = models.CharField(verbose_name=('Direcção do Autocarro'),
                            default='',
                            blank=True)
    route_reg_no = models.CharField(verbose_name=('Direcção do Autocarro'),
                            default='',
                            blank=True)
    customer_profile_name = models.CharField(verbose_name=('Perfil do passageiro'),
                            default='',
                            blank=True)
    card_uid3 = models.CharField(verbose_name=('Codigo do Cartão'),
                            default='',
                            blank=True)
    timestamp = models.TimeField(verbose_name=('Hora de Entrada'),
                            default='',
                            blank=True)
    stationfrom_short_name = models.CharField(verbose_name=('Entrada no Autocarro'),
                            default='',
                            blank=True)
    chout_timestamp = models.TimeField(verbose_name=('Hora de Saida'),
                            default='',
                            blank=True)
    stationto_short_name = models.CharField(verbose_name=('Saida no Autocarro'),
                            default='',
                            blank=True)
    money_value = models.CharField(verbose_name=('Valor Pago'),
                            default='',
                            blank=True)
    transaction_count = models.CharField(verbose_name=('Nº de Transações Diárias'),
                            default='',
                            blank=True)
    money_value1 = models.CharField(verbose_name=('Total do valor pago'),
                            default='',
                            blank=True)
    transaction_count2 = models.CharField(verbose_name=('Total de transações diárias'),
                            default='',
                            blank=True)
    money_value3 = models.DecimalField(verbose_name=('Total de transações diárias'),
                            default='',
                            blank=True)
    bus_nr = models.CharField(verbose_name=('Nº de Autocarro'),
                            default='',
                            blank=True)
    spz = models.CharField(verbose_name=('Matrícula do Autocarro'),
                            default='',
                            blank=True)



    