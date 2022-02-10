from django import forms
from .models import Csv

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CsvModelForm(forms.ModelForm):
	class Meta:
		model = Csv
		fields = ('file_name',)


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email', 'password1', 'password2']
	
	