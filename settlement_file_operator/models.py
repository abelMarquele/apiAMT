from django.db import models

# Create your models here.


class settlement_file_operator(models.Model):
    transaction_type = models.CharField(
                            default='',
                            blank=True)
    money_value = models.DecimalField(
                            default='',
                            blank=True)
    transaction_count = models.IntegerField(
                            default='',
                            blank=True)
    money_value4 = models.DecimalField(
                            default='',
                            blank=True)
    transaction_type2 = models.CharField(
                            default='',
                            blank=True)
    Textbox217 = models.IntegerField(
                            default='',
                            blank=True)
    Textbox214 = models.IntegerField(
                            default='',
                            blank=True)
    Textbox218 = models.IntegerField(
                            default='',
                            blank=True)
    transaction_count3 = models.IntegerField(
                            default='',
                            blank=True)
    Textbox74 = models.DecimalField(
                            default='',
                            blank=True)
    Textbox88 = models.DecimalField(
                            default='',
                            blank=True)
    transaction_count4 = models.IntegerField(
                            default='',
                            blank=True)
    Textbox98 = models.DecimalField(
                            default='',
                            blank=True)
    Textbox100 = models.DecimalField(
                            default='',
                            blank=True)
    rank = models.IntegerField(
                            default='',
                            blank=True)
    carrier_name = models.CharField(verbose_name=('Gestor da Cooperativa'),
                            default='',
                            blank=True)
    cooperatives = models.CharField(verbose_name=('Nome da Cooperativa'),
                            default='',
                            blank=True)
    money_value3 = models.DecimalField(verbose_name=('Receita da Cooperativa'),
                            default='',
                            blank=True)
    Textbox220 = models.DecimalField(
                            default='',
                            blank=True)
    transaction_count2 = models.DecimalField(
                            default='',
                            blank=True)
    Textbox76 = models.DecimalField(
                            default='',
                            blank=True)
    Textbox77 = models.DecimalField(
                            default='',
                            blank=True)