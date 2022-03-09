from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from CSVS.decorators import allowed_users, unauthenticated_user
from CSVS.filters import csvFilter, operator_spzFilter
from CSVS.models import Csv, Profile
from capacity_summary_report.models import capacity_summary_report
from conductor_sales_report.models import conductor_sales_report
from corridor_performance_report.models import corridor_performance_report
from index_translation.models import Assign, Bus, Cooperative, Manager
from passenger_by_bus_and_trip_report.models import passenger_by_bus_and_trip_report
from settlement_file_operator.models import settlement_file_operator
from .forms import CreateUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt

from django.db.models import Count


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
            group = user.groups.all()[0].name
            if group in ['Desenvolvedor']:
                return redirect('schema-swagger-ui')
            else:
                return redirect('csvs:home-view')
        else:
            messages.info(request, 'Nome de usuário OU senha está incorreta')
    
    context = {}
    return render(request, 'login.html', context)

def logoutPage(request):
	logout(request)
	return redirect('csvs:login-view')

@login_required(login_url='csvs:login-view')
def userProfile(request):
	profile = request.user.profile
	form = ProfileForm(instance=profile)

	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'profile.html', context)

@login_required(login_url='csvs:login-view')
def home(request):
    csv = Csv.objects.all()
    capacity_count = capacity_summary_report.objects.all().count()
    conductor_count = conductor_sales_report.objects.all().count()
    corridor_count = corridor_performance_report.objects.all().count()
    passenger_count = passenger_by_bus_and_trip_report.objects.all().count()
    settlement_file_count = settlement_file_operator.objects.all().count()

    assign_count = Assign.objects.all(        
        ).values('cooperativeR','managerR','manager').annotate(
                spz_count=Count('bus'),
            )
    # print(assign_count.query)
    # print(assign_count)

    context = {'capacity_count':capacity_count,'conductor_count':conductor_count,
    'corridor_count':corridor_count,'passenger_count':passenger_count,
    'settlement_file_count':settlement_file_count, 'assign_count':assign_count,
    'csv':csv}
    return render(request, 'dashboard.html', context)

