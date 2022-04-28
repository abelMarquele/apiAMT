from django import forms
from .models import Csv, Profile

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms

class CsvModelForm(forms.ModelForm):
	class Meta:
		model = Csv
		fields = ('file_name',)


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email', 'password1', 'password2']
		include = ['group']

class GroupForm(forms.Form):
	group = forms.ModelChoiceField(queryset=Group.objects.exclude(name='Operador').exclude( name='Desenvolvedor').exclude( name='Admin'))


	
class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['user']
