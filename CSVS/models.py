from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Csv(models.Model):
	file_name = models.FileField(upload_to='csvs')
	uploaded = models.DateTimeField(auto_now_add=True)
	activated = models.BooleanField(default=False)

	def __str__(self):
		return f"File id: {self.id}"


class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True ,on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	emails = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png",null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return str(self.name)