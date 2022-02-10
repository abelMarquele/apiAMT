from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from CSVS.decorators import unauthenticated_user
from .forms import CreateUserForm
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
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

def logoutUser(request):
	logout(request)
	return redirect('csvs:home-view')


def home(request):
    context = {}
    return render(request, 'home.html', context)

