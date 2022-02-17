from django.contrib import admin
from .models import Cooperative, Corridor, Routa, Bus, Manager, Assign


# Register your models here.

admin.site.register(Cooperative)
admin.site.register(Corridor)
admin.site.register(Routa)
admin.site.register(Bus)
admin.site.register(Manager)
admin.site.register(Assign)