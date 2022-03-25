from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from .models import *
# Create your views here.
def student(request):
    return render(request,'student/register.html')
def student_register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        stud_dob=request.POST['DOB']
        stud_phone=request.POST['phone']
        stud_dept_name=request.POST['dept_name']
        stud_branch=request.POST['batch']
        stud_image=request.FILES['images']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if cpassword==password:
            if User.objects.filter(username=username):
                print('ALREADY EXIST')
                return render(request,'student/register.html')
            else:
                user=User(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                student=Student(stud_dob=stud_dob,stud_branch=stud_branch,stud_dept_name=stud_dept_name,stud_image=stud_image,stud_phone=stud_phone,id=user)
                print('SAVED')
                student.save()
                return render(request,'student/welcome.html')
        else:
            print('NOT SAVED ********* PASSWORD NOT MATCH')
            return render(request,'student/register.html')
    else:
        print('DATA MISSED********')
        return render(request,'student/register.html')

def welcome(request):
    return render(request,'student/welcome.html')

