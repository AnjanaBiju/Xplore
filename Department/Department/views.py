
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from hod.models import *
from student.models import *
from django.contrib.auth import login as auth_login
from teacher.models import *
# Create your views here.
@login_required(login_url='login')
def student(request):
    return render(request,'/student/')
def hod(request):
    return render(request,'/hod/')
def login(request):
    return render(request,'login.html')
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print('USERNAME : ',username,'PASSWORD : ',password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            print(user,'USER')
            auth_login(request,user)
            return redirect('welcomes')           
        else:
            print('invalid')
            return redirect('login')

@login_required(login_url='login')
def welcomes(request):
    print(request.user,'********')
    return render(request,'HOD/hod_welcome.html') 
def card_register(request):
    print(request.user)
    return render(request,'cards_register.html')
