import email
from email.mime import image
from tokenize import group
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from hod.models import *
from student.models import *
from . models import *
from django.contrib import messages

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
def placement_notification(request):
    username=request.user.username
    print(username)
    if Placement_coordinator.objects.filter(username=username):
        messages.info(request,'You are allocated as placement coordinator ',extra_tags='messages')
    else:
        messages.info(request,'You are not allocated as placement coordinator ',extra_tags='messages')
        

    return redirect('welcome')

def exam_notifications(request):
    username=request.user.username
    print(username)
    if Exam_coordinator.objects.filter(username=username):
        print('yes')
        messages.info(request,'You are allocated as exam coordinator',extra_tags='messages')

    else:
        print('Not')
        messages.info(request,'You are not allocated as exam coordinator',extra_tags='messages')

    return redirect('welcome')


def time_table_notifications(request):
    username=request.user.username
    print(username)
    if Time_table_coordinator.objects.filter(username=username):
        print('yes')
        messages.info(request,'You are allocated as time table coordinator ',extra_tags='messages')

    else:
        print('Not')
        messages.info(request,'You are not allocated as time table coordinator ',extra_tags='messages')

    return redirect('welcome')


def tutor_notifications(request):
    username=request.user.username
    print(username)
    if Tutor_allocation.objects.filter(tutor=username):
        batch=Tutor_allocation.objects.get(tutor=username)
        print(batch.batch)
        #messages.info(request,'You are allocated as tutor ',extra_tags='messages')
        print('yes')
        return render(request,'Teacher/Tutor/tutor_welcome.html',{'batch':batch})
    else:
        messages.info(request,'You are not allocated as tutor ',extra_tags='messages')

    return redirect('welcome')


def subject_alloc_notification(request):
    username=request.user.username
    print(username)
    if Subject_allocation.objects.filter(tutor=username):
        messages.info(request,'You are allocated for a subject ',extra_tags='messages')
        print('yes')
    else:
        messages.info(request,'You are not allocated for any subjects',extra_tags='messages')

    return redirect('welcome')

def student_list(request):
    print('***student list***')
    username=User.objects.get(username=request.user.username)
    id=username.id
    batch=Tutor_allocation.objects.get(tutor=username) 
    batch=batch.batch
    students=Student.objects.filter(stud_branch=batch)
    print(students,'****')
    return render(request,'Teacher/Tutor/student_list.html',{'students':students,'batch':batch})
