from django.db import models

from index_translation.models import Cooperative, Corridor, Routa


# Create your models here.

class capacity_summary_report(models.Model):
    date = models.DateField(verbose_name=('Data'),
                            blank=True,
                            null=True)
    corridor = models.ForeignKey(Corridor, related_name="capacityCorridor", on_delete=models.SET_NULL, null=True)
    line_nr = models.ForeignKey(Routa, related_name="capacityRouta", on_delete=models.SET_NULL, null=True)
    bus_nr = models.IntegerField(verbose_name=('Nº de Autocarro'),
                            default='',
                            blank=True)
    spz = models.CharField(verbose_name=('Matrícula do Autocarro'),
                            max_length = 50,
                            default='',
                            blank=True)
    no_of_trips = models.IntegerField(verbose_name=('Nº de Autocarro'),
                            default='',
                            blank=True)
    passenger_count = models.IntegerField(verbose_name=('Nº de Autocarro'),
                            default='',
                            blank=True)
    total_income = models.DecimalField(verbose_name=('Receita total'),
                            max_digits = 30,
                            decimal_places = 3,
                            default='',
                            blank=True)
    maxcom_income = models.DecimalField(verbose_name=('Receita da Maxcom'),
                            max_digits = 30,
                            decimal_places = 3,
                            default='',
                            blank=True)
    amt_income = models.DecimalField(verbose_name=('Receita da AMT'),
                            max_digits = 30,
                            decimal_places = 3,
                            default='',
                            blank=True)
    operator_income = models.DecimalField(verbose_name=('Receita da Cooperativa'),
                            max_digits = 30,
                            decimal_places = 3,
                            default='',
                            blank=True)
    cooperative = models.ForeignKey(Cooperative, related_name="capacityCooperative", on_delete=models.SET_NULL, null=True)
    operator = models.CharField(verbose_name=('Gestor da Cooperativa'),
                            max_length = 50,
                            default='',
                            blank=True)
    