# from tokenize import group
import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from CSVS.decorators import allowed_users, unauthenticated_user
from CSVS.models import Csv , Profile
from capacity_summary_report.models import capacity_summary_report
from conductor_sales_report.models import conductor_sales_report
from corridor_performance_report.models import corridor_performance_report
from index_translation.models import Assign, Bus, Cooperative, Manager
from passenger_by_bus_and_trip_report.models import passenger_by_bus_and_trip_report
from settlement_file_operator.models import settlement_file_operator
from .forms import GroupForm, CreateUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from django.db.models import Count


@unauthenticated_user
def registerDeveloper(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Desenvolvedor')
            user.groups.add(group)
            Profile.objects.create(
			    user=user,
			    name=user.username,
			)

        messages.success(request, 'A conta foi criada para '+ username)
        return redirect('csvs:login-view')  

    context = {'form':form}
    return render(request, 'register.html', context)

@unauthenticated_user
@csrf_exempt
def userlogin(request):
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

def userlogout(request):
	logout(request)
	return redirect('csvs:login-view')

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def profile(request):
    profile = request.user.profileUser

    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()   


    context = {'form':form}
    return render(request, 'profile.html',context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    profile = user.profileUser
    manager = user.managerUser
    
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()


    context = {'form':form, 'manager':manager}
    return render(request, 'user_profile.html', context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def registerOperator(request, pk):
    manager = Manager.objects.get(id=pk)
    user = User.objects.get(id=manager.user.id)

    form = CreateUserForm(instance=user)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            Profile.objects.filter(user=user).update(emails=user.email)

        messages.success(request, 'A conta foi alterada :' + manager.operator)

    context = {'form':form, 'manager':manager}

    return render(request, 'user_register.html', context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def registerAdmin(request):
    user = User.objects.filter(groups__name__in=['Maxcom', 'AMT'])
    form = CreateUserForm()
    form1 = GroupForm()
    
    if request.method == 'POST':
        obj, created = User.objects.get_or_create(
			    username = request.POST.get("username", "0"),
                email = request.POST.get("email", "0"),
			    password = request.POST.get("password1", "0"),
			)

        group = Group.objects.get(id= request.POST.get("group", "0"))
        obj.groups.add(group)
        if request.is_ajax():
            return JsonResponse({'message': 'A ação foi realizada com sucesso!'})


    context = {'form':form, 'form1':form1, 'user':user}

    return render(request, 'admin_register.html', context)


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

