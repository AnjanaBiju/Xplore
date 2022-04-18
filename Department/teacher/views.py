import email
from email.mime import image
#from itertools import total
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
        return redirect('placement_welcome')
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
        return redirect('time_table_welcome')

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
        print(request.user.id)
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
def placement_welcome(request):
    return render(request,'Teacher/Placements/placement_welcome.html')
def questions(request):
    user=User.objects.get(username=request.user)
    id=user.id
    coordinator=Teacher.objects.get(id=id)
    dept_name=coordinator.teach_dept_name
    return render(request,'Teacher/Placements/Questions_upload.html',{'dept_name':dept_name})
def add_questions(request):
    if request.method=='POST':
        Dept_name=request.POST['Dept_name']
        Subject=request.POST['Subject']
        Question=request.POST['Question']
        OptionA=request.POST['OptionA']
        OptionB=request.POST['OptionB']
        OptionC=request.POST['OptionC']
        OptionD=request.POST['OptionD']
        Answer=request.POST['Answer']
        Level=request.POST['Level']
        Score=request.POST['Score']
        question=Questions(Dept_name=Dept_name,Subject=Subject,Question=Question,OptionA=OptionA,OptionB=OptionB,OptionC=OptionC,OptionD=OptionD,answer=Answer,Score=Score,Level=Level)
        question.save()
        print('saved')
        return redirect('questions')
    else:
        return render(request,'Teacher/Placements/Questions_upload.html')

def show_questions(request):
    id=request.user.id
    #print(id,'***')
    tutor=Teacher.objects.get(id=id)
    dept=tutor.teach_dept_name
    questions=Questions.objects.filter(Dept_name=dept)
    return render(request,'Teacher/Placements/Questions.html',{'questions':questions})
def time_table_welcome(request):
    return render(request,'Teacher/Time_table/time_table_welcome.html')
def time_table_generation(request):
    id=request.user.id
    tutor=Teacher.objects.get(id=id)
    dept=tutor.teach_dept_name
    return render(request,'Teacher/Time_table/upload_timetable.html',{'dept':dept})
def attendance_marking(request):
    id=request.user.id
    tutor=Teacher.objects.get(id=id)
    dept=tutor.teach_dept_name
    if Tutor_allocation.objects.filter(tutor=request.user.username).exists():
        tutor=Tutor_allocation.objects.get(tutor=request.user.username)
        batch=tutor.batch
    else:
        if Subject_allocation.objects.filter(tutor=request.user.username).exists():
            tutor=Subject_allocation.objects.get(tutor=request.user.username)
            batch=tutor.batch
    
    #stud_batch==tutor.teach_batch
    students=Student.objects.filter(stud_dept_name=dept,stud_branch=batch)
    return render(request,'Teacher/Attendance/attendance.html',{'students':students})