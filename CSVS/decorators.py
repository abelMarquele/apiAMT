from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args,**kwargs):
		if request.user.is_authenticated:
			return redirect('csvs:home-view')
		else:
			return view_func(request, *args,**kwargs)
	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args,**kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group in allowed_roles:
				return view_func(request, *args,**kwargs)
			else:
				return HttpResponse('Você não está autorizado a visualizar esta página')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_func(request, *args,**kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
		if group == "Admin" or group == "AMT" or group == "Maxcom":
			return view_func(request, *args,**kwargs)
		else:
			return redirect('csvs:home-view')
	return wrapper_func