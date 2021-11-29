from django.urls import path
from.import views
from .views import home_view


app_name='CSVS'

urlpatterns = [
	path('',home_view, name='home'),
	path('home/', home_view, name = 'home-view'),
]