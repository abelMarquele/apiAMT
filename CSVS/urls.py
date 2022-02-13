from django.urls import path
from .views import home, logoutPage, registerPage, loginPage, userProfile

app_name='CSVS'

urlpatterns = [
	path('', home, name='home-view'),
	path('register/', registerPage, name='register-view'),
    path('login/', loginPage, name='login-view'),
	path('logout/', logoutPage, name='logout-view'),
	path('profile/', userProfile, name='profile-view'),
]