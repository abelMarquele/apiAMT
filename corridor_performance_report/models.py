from django.db import models

from index_translation.models import Cooperative, Corridor, Routa, Bus

# Create your models here.

class corridor_performance_report(models.Model):
    date = models.DateField(verbose_name=('Data'),
                            blank=True,
                            null=True)
    corridor = models.ForeignKey(Corridor, related_name="corridorCorridor", on_delete=models.SET_NULL, null=True)
    line_nr = models.ForeignKey(Routa, related_name="corridorRouta", on_delete=models.SET_NULL, null=True)
    line_nr_1 = models.CharField(verbose_name=('Routa'),
                            max_length= 50,
                            default='',
                            blank=True)
    bus_nr = models.IntegerField(verbose_name=('Nº de Autocarro'),
                            default='',
                            blank=True)
    spz = models.ForeignKey(Bus, related_name="corridorBus", null=True, blank=True, on_delete=models.SET_NULL)
    spz_1 = models.CharField(verbose_name=('Matrícula'),
                            max_length= 50,
                            default='',
                            blank=True)
    cooperative = models.ForeignKey(Cooperative, related_name="corridorCooperative", on_delete=models.SET_NULL, null=True)
    operator = models.CharField(verbose_name=('Gestor'),
                            max_length= 50,
                            default='',
                            blank=True)
    passenger_count = models.IntegerField(verbose_name=('Nº de Passageiros'),
                            null= True,
                            blank=True)
    luggage_count = models.IntegerField(verbose_name=('Nº de Bagagem'),
                            null= True,
                            blank=True)
    qr_ticket_count = models.IntegerField(verbose_name=('Nº de Tickets'),
                            null= True,
                            blank=True)
    amount_ticket = models.DecimalField(verbose_name=('Receita de Tickets'),
                            max_digits = 30,
                            decimal_places = 3,
                            null= True,
                            blank=True)
    amount_luggage = models.DecimalField(verbose_name=('Receita de Bagagem'),
                            max_digits = 30,
                            decimal_places = 3,
                            null= True,
                            blank=True)
    maxcom_income = models.DecimalField(verbose_name=('Receita da Maxcom'),
                            max_digits = 30,
                            decimal_places = 3,
                            null= True,
                            blank=True)
    amt_income = models.DecimalField(verbose_name=('Receita da AMT'),
                            max_digits = 30,
                            decimal_places = 3,
                            null= True,
                            blank=True)
    operator_income = models.DecimalField(verbose_name=('Receita da Cooperativa'),
                            max_digits = 30,
                            decimal_places = 3,
                            null= True,
                            blank=True)


