from django.db import models

from index_translation.models import Routa

# Create your models here.



class passenger_by_bus_and_trip_report(models.Model):
    timestamp1 = models.DateField(verbose_name=('Data'),
                            blank=True,
                            null=True)
    device_location1 = models.CharField(verbose_name=('ID e Matrícula do Autocarro'),
                            max_length=50,
                            default='',
                            blank=True)
    line_reg_no1 = models.ForeignKey(Routa, related_name="passengerRouta", on_delete=models.SET_NULL, null=True)
    route_reg_no1 = models.IntegerField(verbose_name=('Direcção do Autocarro'),
                            max_length=50,
                            default='',
                            blank=True)
    route_reg_no = models.IntegerField(verbose_name=('Direcção do Autocarro'),
                            max_length=50,
                            default='',
                            blank=True)
    customer_profile_name = models.CharField(verbose_name=('Perfil do passageiro'),
                            max_length=50,
                            default='',
                            blank=True)
    card_uid3 = models.CharField(verbose_name=('Codigo do Cartão'),
                            max_length= 50,
                            default='',
                            blank=True)
    timestamp = models.TimeField(verbose_name=('Hora de Entrada'),
                            default='',
                            blank=True)
    stationfrom_short_name = models.CharField(verbose_name=('Entrada no Autocarro'),
                            max_length=50,
                            default='',
                            blank=True)
    chout_timestamp = models.TimeField(verbose_name=('Hora de Saida'),
                            default='',
                            blank=True)
    stationto_short_name = models.CharField(verbose_name=('Saida no Autocarro'),
                            max_length=50,
                            default='',
                            blank=True)
    money_value = models.DecimalField(verbose_name=('Valor Pago'),
                            max_digits = 7,
                            decimal_places = 3,
                            default='',
                            blank=True)
    transaction_count = models.IntegerField(verbose_name=('Nº de Transações Diárias'),
                            default='',
                            blank=True)
    money_value1 = models.DecimalField(verbose_name=('Total do valor pago'),
                            max_digits = 7,
                            decimal_places = 3,
                            default='',
                            blank=True)
    transaction_count2 = models.IntegerField(verbose_name=('Total de transações diárias'),
                            default='',
                            blank=True)
    money_value3 = models.DecimalField(verbose_name=('Total de transações diárias'),
                            max_digits = 7,
                            decimal_places = 3,
                            default='',
                            blank=True)
    bus_nr = models.IntegerField(verbose_name=('Nº de Autocarro'),
                            default='',
                            blank=True)
    spz = models.CharField(verbose_name=('Matrícula do Autocarro'),
                            max_length=50,
                            default='',
                            blank=True)



    