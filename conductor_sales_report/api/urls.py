from django.urls import path
from conductor_sales_report.views import conductor_view

urlpatterns = [
    path('conductor/',conductor_view, name='conductor-view'),
]
