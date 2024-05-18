from django.urls import path
from capacity_summary_report.views import capacity_view

urlpatterns = [
    path('capacity/',capacity_view, name='capacity-view'),
]

