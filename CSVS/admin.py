from django.contrib import admin
from .models import Csv, Profile, Log_login, Log_event

admin.site.register(Csv)
admin.site.register(Profile)
admin.site.register(Log_login)
admin.site.register(Log_event)