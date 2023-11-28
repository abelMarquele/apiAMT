from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from index_translation.models import Manager,Cooperative
from .models import Log_login, Profile

from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out

# Metodo que faz registo na basa de dados sempre que um usuario faz log in do sistema
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
	print('user {} logged in through page {}'.format(user.username, request.META.get('HTTP_REFERER')))
	info = request.user_agent
	if request.user_agent.is_mobile:
		Log_login.objects.create(
		user=user,
		event_type=1,
		device_type=1,
		)
	elif request.user_agent.is_tablet:
		Log_login.objects.create(
		user=user,
		event_type=1,
		device_type=2,
		)
	elif request.user_agent.is_pc:
		Log_login.objects.create(
		user=user,
		event_type=1,
		device_type=3,
		)
	elif request.user_agent.is_touch_capable:
		Log_login.objects.create(
		user=user,
		event_type=1,
		device_type=4,
		)
	elif request.user_agent.is_bot:
		Log_login.objects.create(
		user=user,
		event_type=1,
		device_type=5,
		)

# Metodo que faz registo na basa de dados sempre que um usuario faz log out do sistema 
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
	print('user {} logged out through page {}'.format(user.username, request.META.get('HTTP_REFERER')))
	info = request.user_agent
	if request.user_agent.is_mobile:
		Log_login.objects.create(
		user=user,
		event_type=0,
		device_type=1,
		)
	elif request.user_agent.is_tablet:
		Log_login.objects.create(
		user=user,
		event_type=0,
		device_type=2,
		)
	elif request.user_agent.is_pc:
		Log_login.objects.create(
		user=user,
		event_type=0,
		device_type=3,
		)
	elif request.user_agent.is_touch_capable:
		Log_login.objects.create(
		user=user,
		event_type=0,
		device_type=4,
		)
	elif request.user_agent.is_bot:
		Log_login.objects.create(
		user=user,
		event_type=0,
		device_type=5,
		)

# Metodo que faz o adiciona o grupo e cria o perfil do usuario.
def user_profile(sender, instance, created,**kwargs):
	if created:
		if instance.is_superuser:
			group = Group.objects.get(name='Admin')
			instance.groups.add(group)
			obj, created = Profile.objects.get_or_create(
				user=instance,
				name=instance.username,
			)

		if instance.is_staff and instance.is_superuser == False:
			group = Group.objects.get(name='Operador')
			instance.groups.add(group)
			obj, created = Profile.objects.get_or_create(
				user=instance,
				name=instance.username,
				)
			Manager.objects.filter(abbreviated=instance.username).update(user=instance)

		if instance.is_staff == False and instance.is_superuser == False and instance.is_active == False:
			group = Group.objects.get(name='Cooperativa')
			instance.groups.add(group)
			obj, created = Profile.objects.get_or_create(
				user=instance,
				name=instance.username,
				)
			Cooperative.objects.filter(cooperative=instance.username).update(user=instance)

def manager_profile(sender, instance, created, **kwargs):
	if created:
		obj, created = User.objects.get_or_create(
			username=instance.abbreviated,
			is_staff = False,
			)
		usr = User.objects.get(username=instance.abbreviated)
		usr.set_password('amt12345678')
		usr.save()

# Metodo que faz a criar de um usuario ao criar a cooperativa e atribuir a senha padrão 'amt12345678' Não testado 
def cooperative_profile(sender, instance, created, **kwargs):
	if created:
		obj, created = User.objects.get_or_create(
			username=instance.cooperative,
			is_staff = False,
			is_superuser = False,
			is_active = False,
			)
		usr = User.objects.get(username=instance.cooperative)
		usr.set_password('amt12345678')
		usr.save()

post_save.connect(user_profile, sender=User)
post_save.connect(manager_profile, sender=Manager)
post_save.connect(cooperative_profile, sender=Cooperative)
