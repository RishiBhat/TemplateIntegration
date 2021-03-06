
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import SigninForm, RegisterForm


def login_view(request):
    form = SigninForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password") 
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/main/dash")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    
    return render(request, "signin.html", {"form": form, "msg" : msg})




def register_user(request):
    msg     = None
    success = False

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form, "msg" : msg, "success" : success })




#Now integrating the dashboard from the temopplate 


def dash(request):
    return render(request,'main/dashindex.html')



def about(request):
    return render(request,'main/about.html')