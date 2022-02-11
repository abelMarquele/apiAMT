from django.urls import path, re_path
from .views import home, registerPage, loginPage, userProfile

from django.contrib.auth import views as auth_views
from rest_auth.views import PasswordResetConfirmView

app_name='CSVS'

urlpatterns = [
	path('', home, name='home-view'),
	path('register/', registerPage, name='register-view'),
    path('login/', loginPage, name='login-view'),
	path('logout/', loginPage, name='logout-view'),
	path('profile/', userProfile, name='profile-view'),

	# re_path(r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
    #         name='rest_password_reset_confirm'),

	path('reset_password/',
     	auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     	name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     	auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     	name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

	# path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),

    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]