from django.db import models

from index_translation.models import Cooperative, Corridor, Routa

# Create your models here.

class corridor_performance_report(models.Model):
    date = models.DateField(verbose_name=('Data'),
                            blank=True,
                            null=True)
    corridor = models.ForeignKey(Corridor, related_name="capacityCorridor", on_delete=models.SET_NULL, null=True)
    line_nr = models.ForeignKey(Routa, related_name="capacityRouta", on_delete=models.SET_NULL, null=True)
    bus_nr = models.CharField(verbose_name=('Nº de Autocarro'),
                            default='',
                            blank=True)
    spz = models.CharField(verbose_name=('Matrícula do Autocarro'),
                            default='',
                            blank=True)
    cooperative = models.ForeignKey(Cooperative, related_name="capacityCooperative", on_delete=models.SET_NULL, null=True)
    operator = models.CharField(verbose_name=('Gestor da Cooperativa'),
                            default='',
                            blank=True)
    passenger_count = models.CharField(verbose_name=('Nº de Passageiros'),
                            default='',
                            blank=True)
    luggage_count = models.CharField(verbose_name=('Nº de Bagagem'),
                            default='',
                            blank=True)
    qr_ticket_count = models.CharField(verbose_name=('Nº de Tickets'),
                            default='',
                            blank=True)
    amount_ticket = models.DecimalField(verbose_name=('Receita de Tickets'),
                            default='',
                            blank=True)
    amount_luggage = models.DecimalField(verbose_name=('Receita de Bagagem'),
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

  