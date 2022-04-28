from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from index_translation.models import Manager
from .models import Log_login, Profile

from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out

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

def user_profile(sender, instance, created,**kwargs):
	if created:
		if instance.is_superuser:
			group = Group.objects.get(name='Admin')
			instance.groups.add(group)
			obj, created = Profile.objects.get_or_create(
				user=instance,
				name=instance.username,
			)

		if instance.is_staff and instance.is_superuser==False:
			group = Group.objects.get(name='Operador')
			instance.groups.add(group)
			obj, created = Profile.objects.get_or_create(
				user=instance,
				name=instance.username,
				)
			Manager.objects.filter(abbreviated=instance.username).update(user=instance)
		# print('user_profile', created)

def manager_profile(sender, instance, created, **kwargs):
	if created:
		obj, created = User.objects.get_or_create(
			username=instance.abbreviated,
			password='amt12345678',
			is_staff = True,
			)
	# print('manager_profile', created)

post_save.connect(user_profile, sender=User)
post_save.connect(manager_profile, sender=Manager)
