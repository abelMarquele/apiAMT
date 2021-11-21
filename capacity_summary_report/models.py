from django.db import models

from index_translation.models import Cooperative, Corridor, Routa


# Create your models here.

class capacity_summary_report(models.Model):
    date = models.DateField(verbose_name=('Data'),
                            blank=True,
                            null=True)
    corridor = models.ForeignKey(Corridor, related_name="capacityCorridor", on_delete=models.SET_NULL, null=True)
    line_nr = models.ForeignKey(Routa, related_name="capacityRouta", on_delete=models.SET_NULL, null=True)
    bus_nr = models.CharField(verbose_name=('Nº de Autocarro'),
                            max_length=4,
                            default='',
                            blank=True)
    spz = models.CharField(verbose_name=('Matrícula do Autocarro'),
                            max_length=15,
                            default='',
                            blank=True)
    no_of_trips = models.CharField(verbose_name=('Nº de Autocarro'),
                            max_length=2,
                            default='',
                            blank=True)
    passenger_count = models.CharField(verbose_name=('Nº de Autocarro'),
                            default='',
                            blank=True)
    total_income = models.DecimalField(verbose_name=('Receita total'),
                            default='',
                            blank=True)
    maxcom_income = models.DecimalField(verbose_name=('Receita da Maxcom'),
                            default='',
                            blank=True)
    amt_income = models.DecimalField(verbose_name=('Receita da AMT'),
                            default='',
                            blank=True)
    operator_income = models.DecimalField(verbose_name=('Receita da Cooperativa'),
                            default='',
                            blank=True)
    cooperative = models.ForeignKey(Cooperative, related_name="capacityCooperative", on_delete=models.SET_NULL, null=True)
    operator = models.CharField(verbose_name=('Gestor da Cooperativa'),
                            max_length=100,
                            default='',
                            blank=True)
    