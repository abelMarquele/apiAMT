from django.urls import path
from .views import registerAdmin, userlogout, registerDeveloper, userlogin, userProfile, profile, registerOperator, cooperativeProfile, registerCooperative

from . import views

app_name='CSVS'

urlpatterns = [
    path("", views.index, name='dashboard'),
	path('register/', registerDeveloper, name='register-view'),
	path('user_register/<str:pk>/', registerOperator, name='user_register-view'),
    path('user_cooperative_register/<str:pk>/', registerCooperative, name='user_cooperative_register-view'),
	path('admin_register/', registerAdmin, name='admin_register-view'),
	path('user_profile/<str:pk>/', userProfile, name='user_profile-view'),
    path('cooperative_profile/<str:pk>/', cooperativeProfile, name='cooperative_profile-view'),
    path('login/', userlogin, name='login-view'),
	path('logout/', userlogout, name='logout-view'),
	path('profile/', profile, name='profile-view'),
]