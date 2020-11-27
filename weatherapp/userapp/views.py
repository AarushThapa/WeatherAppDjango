from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm

# def register(request):


def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/')
    else:
        form = LoginForm
        template_name = 'user/login.html'
        context = {
            'form' : form
        }
        return render(request,template_name, context)


def logoutAction(request):
    logout(request)
    return redirect('/')