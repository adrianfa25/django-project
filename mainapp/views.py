from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
#Import library to register user
from .forms import RegisterForm
#Improt register Form

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
#Import login and logout

from django.contrib.auth.decorators import login_required
#Decorator for login required

@login_required(login_url='login')
def userdata(request):

    if request.user.is_staff:
        state = "Is admin"
    else: 
        state = "Is not admin"
    return render(request, 'users/userdata.html',{
        'title': 'User data',
        'state': state
    })



def index(request):
    return render (request, 'mainapp/index.html',{
        'title': 'The best cinema page'
    })

def register_page(request):

    #Register form personalized
    if request.user.is_authenticated:
        return redirect('index')

    else:
        register_form = RegisterForm()

    #If receive post methos:

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

    #If receive form and is valid, save the dates
        
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Your register was successful!!')

            return redirect('index')


    return render(request, 'users/register.html',{
        'title': 'Register',
        'register_form': register_form
    })



def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            messages.success(request, 'Your login was successful!!')

            user = authenticate(request, username=username, password=password)
            #utilizamos los Keyboard Arguments y justo son iguales a lo que nosotros estabamos llamando.
            if user is not None:
                login(request, user)

                return redirect('index')
            else:
                messages.warning(request, 'Could not Log in!')

        return render(request, 'users/login.html',{
            'title': 'Login'
            })


def logout_user(request):
    logout(request)
    return redirect('login')