import email
from email.mime import image
from tokenize import group
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from . models import *

def teacher(request):
    return render(request,'Teacher/teach_register.html')
def teacher_register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        dept_name=request.POST['dept_name']
        dob=request.POST['DOB']
        designation=request.POST['designation']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        images=request.FILES['images']
        if cpassword==password:
            if User.objects.filter(username=username):
                print('ALREADY EXIST')
                return redirect('teacher_register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                teacher=Teacher(teach_dept_name=dept_name,teach_dob=dob,group=1,teach_designation=designation,teach_phone=phone,teach_image=images,id=user)
                teacher.save()
                return redirect('login')
        else:
            print('WRONG PASSWORD')
            return redirect('teacher')
    else:
        return redirect('teacher')
login_required(login_url='login')
def welcome(request):
    return render(request,'Teacher/teach_welcome.html')
login_required(login_url='login')
def attendance_marking(request):
    print(request.user,'********************************************')
    return render(request,'Teacher/attendance_marking.html')

