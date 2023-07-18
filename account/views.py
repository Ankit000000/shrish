from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import  login as login_auth
from django.contrib.auth.models import  auth
from django.contrib.auth.hashers import make_password
# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()
def logout(request):
    auth.logout(request)
    return redirect("/")

def login(request):
    if request.method == "POST" :
        username=request.POST["username"]
        password1=request.POST["password"]
        user=auth.authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credential")
            return redirect("login")
    return render(request,"login.html")

def register(request):
    if request.method == "POST" :
        firstname=request.POST["Full_Name"]
        lastname=request.POST["lastname"]
        mail=request.POST["mail"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        usertype=request.POST["usertype"]
        phone=request.POST["phone"]
        if (password1==password2):
            if (User.objects.filter(first_name=firstname)).exists():
                messages.info(request,"name taken")
                return redirect("register")
            elif (User.objects.filter(email=mail)).exists():
                messages.info(request,"mail taken")
                return redirect("register")
            else:
                password1 = make_password(password1)
                user=User(password=password1,first_name=firstname,last_name=lastname,usertype=usertype,email=mail,phone=phone,username=firstname )
                user.save()
                # print(user.email)
                return render(request,"login.html")
        else:
            messages.info(request,"Password mismatched")
            return redirect("register")
    else:
        return render(request,"register.html")
    
def home(request):
    return redirect("/")