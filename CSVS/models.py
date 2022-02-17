from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Csv(models.Model):
	NOME = (
		('Capacity summary report','Capacity summary report'),
		('Conductor Sales Report','Conductor Sales Report'),
		('Corridor performance report','Corridor performance report'),
		('Passenger by bus and trip report','Passenger by bus and trip report'),
		('Settlement file operator','Settlement file operator'),
		('Cooperarive','Cooperarive'),
		('Corridor','Corridor'),
		('Routa','Routa'),
		('Assign','Assign'),
		('Manager','Manager'),
		('Bus','Bus'),
	)
	name = models.CharField(verbose_name=('Nome do Ficheiro'),
							choices=NOME,
							max_length=50,
							default='',
							null= True,
                            blank=True)
	file_name = models.FileField(verbose_name=('Ficheiro'),
							upload_to='static/csvs')
	uploaded = models.DateTimeField(auto_now_add=True)
	activated = models.BooleanField(default=False)
	file_row = models.IntegerField(verbose_name=('Nº de Linhas'),
							null= True,
                            blank=True)

	def __str__(self):
		return str(self.file_name)

	@property
	def filesize(self):
		x = self.file_name.size
		y = 512000
		if x < y:
			value = round(x/1000, 2)
			ext = ' kb'
		elif x < y*1000:
			value = round(x/1000000, 2)
			ext = ' Mb'
		else:
			value = round(x/1000000000, 2)
			ext = ' Gb'
		return str(value)+ext

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True ,on_delete=models.CASCADE)
	name = models.CharField(verbose_name=('Nome'), max_length=200, null=True)
	phone = models.CharField(verbose_name=('Nº de Telefone'), max_length=200, null=True)
	emails = models.CharField(verbose_name=('Email'), max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png",null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return str(self.name)