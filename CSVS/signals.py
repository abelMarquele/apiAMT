from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Log_login, Profile

from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
 

# from django.core.signals import request_started, request_finished


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
	
	# print('Despositivo info:  ',info)

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
	
	# print('Despositivo info:  ',info)

def user_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='Desenvolvedor')
		instance.groups.add(group)
		Profile.objects.create(
			user=instance,
			name=instance.username,
			)

		# print('Profile created!')

post_save.connect(user_profile, sender=User)
