from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from CSVS.decorators import allowed_users, unauthenticated_user
from CSVS.filters import csvFilter
from CSVS.models import Csv, Profile
from .forms import CreateUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

        messages.success(request, 'A conta foi criada para '+ username)
        return redirect('csvs:login-view')  

    context = {'form':form}
    return render(request, 'register.html', context)

@unauthenticated_user
@csrf_exempt
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username,password =password)

        if user is not None:
            login(request, user)
            return redirect('csvs:home-view')
        else:
            messages.info(request, 'Nome de usuário OU senha está incorreta')
    
    context = {}
    return render(request, 'login.html', context)

def logoutPage(request):
	logout(request)
	return redirect('csvs:login-view')

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['Gestor'])
def userProfile(request):
	profile = request.user.profile
	form = ProfileForm(instance=profile)

	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES,instance=profile)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'profile.html', context)

@login_required(login_url='csvs:login-view')
def home(request):
    csv = Csv.objects.all()

    myFilter = csvFilter(request.GET, queryset=csv)
    csv = myFilter.qs

    context = {'csv':csv, 'myFilter':myFilter}
    return render(request, 'dashboard.html', context)

