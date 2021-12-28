from django.contrib import admin

from .models import corridor_performance_report


# Register your models here.

#admin.site.register(corridor_performance_report)

# Define the admin class
class corridor_performance_reportAdmin(admin.ModelAdmin):
     list_display = ('date', 'corridor', 'spz', 'cooperative', 'operator')

# Register the admin class with the associated model
admin.site.register(corridor_performance_report, corridor_performance_reportAdmin)