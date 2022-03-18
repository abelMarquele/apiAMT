from django.urls import path
from .views import home, logoutPage, registerPage, loginPage, userProfile, profile, userRegister

app_name='CSVS'

urlpatterns = [
	path('', home, name='home-view'),
	path('register/', registerPage, name='register-view'),
	path('user_register/<str:pk>/', userRegister, name='user_register-view'),
	path('user_profile/', userProfile, name='user_profile-view'),
    path('login/', loginPage, name='login-view'),
	path('logout/', logoutPage, name='logout-view'),
	path('profile/', profile, name='profile-view'),
]