from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from teacher.models import *
# Create your views here.

def login(request):
    return render(request,'login.html')
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print('USERNAME : ',username,'PASSWORD : ',password)
        user=auth.authenticate(username=username,password=password)
        print(user,'USER')
        if user is not None:
            print(user,'USER')
            auth.login(request,user)
            print("valid")
            return redirect('welcome')
        else:
            print('invalid')
            return redirect('login')
@login_required(login_url='login')
def student(request):
    return render(request,'/student/')
@login_required(login_url='login')
def welcome(request):
    return render(request,'student/welcome.html') 