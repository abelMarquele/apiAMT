from django.urls import path
from .views import home, userlogout, registerDeveloper, userlogin, userProfile, profile, registerOperator

app_name='CSVS'

urlpatterns = [
	path('', home, name='home-view'),
	path('register/', registerDeveloper, name='register-view'),
	path('user_register/<str:pk>/', registerOperator, name='user_register-view'),
	path('user_profile/<str:pk>/', userProfile, name='user_profile-view'),
    path('login/', userlogin, name='login-view'),
	path('logout/', userlogout, name='logout-view'),
	path('profile/', profile, name='profile-view'),
]