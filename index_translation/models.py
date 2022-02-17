from django.db import models

# Create your models here.

class Corridor(models.Model):
    corridor = models.CharField(verbose_name=('Nome do Corridor'),
                        max_length=50,
                        unique=True,
                        default='',
                        blank=True)
    def __str__(self):
        return str(self.corridor)

class Routa(models.Model):
    routa = models.CharField(verbose_name=('Nome da Routa'),
                        max_length=50,
                        default='',
                        blank=True)
    via = models.CharField(verbose_name=('Nome da Via'),
                        max_length=50,
                        default='',
                        blank=True)
    corridor = models.ForeignKey(Corridor, related_name="routaCorridor", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.routa)


class Bus(models.Model):
    bus_nr = models.IntegerField(verbose_name=('Nº de Autocarro'),
                            null=True,
                            blank=True)
    spz = models.CharField(verbose_name=('Matrícula'),                     
                            unique=True,
                            blank=False, 
                            null=False,
                            max_length=50)
    brand = models.CharField(verbose_name=('Marca'),
                            max_length=50,
                            default='',
                            blank=True)
    def __str__(self):
        return str(self.spz)
    


class Cooperative(models.Model):
    cooperative = models.CharField(verbose_name=('Nome da Cooperativa'),
                        max_length= 50,
                        unique=True,
                        default='',
                        blank=True)
    def __str__(self):
	    return str(self.cooperative)

class Manager(models.Model):
    operator = models.CharField(verbose_name=('Gestor'),
                        max_length=100,
                        unique=True,
                        default='',
                        blank=True)
    abbreviated = models.CharField(verbose_name=('Nome Abreviado'),
                        max_length=50,
                        default='',
                        blank=True)
    def __str__(self):
        return str(self.operator)


class Assign(models.Model):
    bus = models.ForeignKey(Bus, related_name="assignBus", on_delete=models.SET_NULL, null=True)
    cooperative = models.ForeignKey(Cooperative, related_name="assignCooperative", on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey(Manager, related_name="assignManager", on_delete=models.SET_NULL, null=True)
    cooperativeR = models.CharField(verbose_name=('Nome Da Cooperativa'),
                        max_length=100,
                        default='',
                        blank=True)
    managerR = models.CharField(verbose_name=('Nome do Gestor'),
                        max_length=100,
                        default='',
                        blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    activated = models.BooleanField(verbose_name=('Atribuir'), default=False)
    
    # def __str__(self):
    #     return str(self.bus)