from django.urls import path
from settlement_file_operator.views import settlement_view

urlpatterns = [
    path('settlement_file/',settlement_view, name='settlement_file-view'),
]

