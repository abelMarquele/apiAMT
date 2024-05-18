from django.db import models
from index_translation.models import Cooperative

class settlement_file_operator(models.Model):
    date = models.DateField(verbose_name=('Data'),
                            blank=True,
                            null=True)
    transaction_type = models.CharField(max_length=50,
                            default='',
                            null=True,
                            blank=True)
    money_value = models.DecimalField(max_digits = 30,
                            decimal_places = 3,
                            default='',
                            null=True,
                            blank=True)
    transaction_count = models.IntegerField(
                            default='',
                            null=True,
                            blank=True)
    money_value4 = models.DecimalField(max_digits = 30,
                            decimal_places = 3,
                            default='',
                            null=True,
                            blank=True)
    transaction_type2 = models.CharField(max_length=50,
                            default='',
                            null=True,
                            blank=True)
    Textbox217 = models.IntegerField(
                            default='',
                            null=True,
                            blank=True)
    Textbox214 = models.IntegerField(
                            default='',
                            null=True,
                            blank=True)
    Textbox218 = models.IntegerField(
                            default='',
                            null=True,
                            blank=True)
    transaction_count3 = models.IntegerField(
                            default='',
                            null=True,
                            blank=True)
    Textbox74 = models.DecimalField(max_digits = 30,
                            decimal_places = 3,
                            default='',
                            null=True,
                            blank=True)
    Textbox88 = models.DecimalField(max_digits = 30,
                            decimal_places = 3,
                            default='',
                            null=True,
                            blank=True)
    transaction_count4 = models.IntegerField(
                            default='',
                            null=True,
                            blank=True)
    Textbox98 = models.DecimalField(max_digits = 30,
                            decimal_places = 3,
                            default='',
                            null=True,
                            blank=True)
    Textbox100 = models.DecimalField(max_digits = 30,
                            decimal_places = 3,
                            default='',
                            null=True,
                            blank=True)
    rank = models.IntegerField(
                            default='',
                            null=True,
                            blank=True)
    carrier_name = models.CharField(verbose_name=('Gestor'),
                            max_length=50,
                            default='',
                            null=True,
                            blank=True)
    cooperatives = models.CharField(verbose_name=('Cooperativa'),
                            max_length=50,
                            default='',
                            null=True,
                            blank=True)
    money_value3 = models.DecimalField(verbose_name=('Receita da Cooperativa'),
                            max_digits = 30,
                            decimal_places = 3,
                            default='',
                            null=True,
                            blank=True)
    Textbox220 = models.DecimalField(max_digits = 30,
                            decimal_places = 3,
                            default='',
                            null=True,
                            blank=True)
    transaction_count2 = models.DecimalField(max_digits = 30,
                            decimal_places = 3,
                            default='',
                            null=True,
                            blank=True)
    Textbox76 = models.DecimalField(max_digits = 30,
                            decimal_places = 3,
                            default='',
                            null=True,
                            blank=True)
    Textbox77 = models.DecimalField(max_digits = 30,
                            decimal_places = 3,
                            default='',
                            null=True,
                            blank=True)