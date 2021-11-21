from django.db import models

# Create your models here.


class Cooperative(models.Model):
    cooperative = models.CharField(verbose_name=('Nome da Cooperativa'),
                        max_length=100,
                        default='',
                        blank=True)

class Corridor(models.Model):
    corridor = models.CharField(verbose_name=('Nome do Corridor'),
                        max_length=100,
                        default='',
                        blank=True)

class Routa(models.Model):
    routa = models.CharField(verbose_name=('Nome da Routa'),
                        max_length=100,
                        default='',
                        blank=True)
    via = models.CharField(verbose_name=('Nome da Via'),
                        max_length=100,
                        default='',
                        blank=True)
    corridor = models.ForeignKey(Corridor, related_name="routaCorridor", on_delete=models.SET_NULL, null=True)

