from django.db import models
from index_translation.models import Bus

# Create your models here.

class conductor_sales_report(models.Model):
    company_id = models.IntegerField(verbose_name=('Nº Cooperativa'),
                            default='',
                            blank=True)
    company_name = models.CharField(verbose_name=('Cooperativa'),
                            max_length=50,
                            default='',
                            blank=True)
    device = models.CharField(verbose_name=('Nº do Dispositivo'),
                            max_length=50,
                            default='',
                            blank=True)
    conductor_id = models.IntegerField(verbose_name=('ID do Gestor'),
                            default='',
                            blank=True)
    conductor_first_name = models.ForeignKey(Bus, related_name="conductorBus", null=True, blank=True, on_delete=models.SET_NULL)
    conductor_last_name = models.CharField(verbose_name=('Gestor'),
                            max_length=50,
                            default='',
                            blank=True)
    number = models.IntegerField(verbose_name=('Total de passageiros'),
                            default='',
                            blank=True)
    amount = models.DecimalField(verbose_name=('Receita da Cooperativa'),
                            max_digits = 30,
                            decimal_places = 3,
                            default='',
                            blank=True)
    date = models.DateField(verbose_name=('Data'),
                            blank=True,
                            null=True)

   