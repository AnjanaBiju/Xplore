from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
#from Department.teacher.models import Teacher
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from teacher.models import *
from .models import *
# Create your views here.
def hod(request):
    return render(request,'HOD/hod_register.html')
def hod_register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        hod_dob=request.POST['DOB']
        email=request.POST['email']
        hod_dept_name=request.POST['dept_name']
        hod_phone=request.POST['phone']
        hod_qualification=request.POST['qualification']
        hod_image=request.FILES['images']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if cpassword==password:
            if User.objects.filter(username=username):
                print('already exist')
                return render(request,'cards_register.html')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                hod=Hod(hod_dob=hod_dob,hod_dept_name=hod_dept_name,hod_phone=hod_phone,hod_qualification=hod_qualification,hod_image=hod_image,hod_group=2,id=user)
                hod.save()
                print('saved')
                return render(request,'login.html')
        else:
            print('Wrong password')
            return render(request,'login.html')
    else:
        print('something went wrong')
        return render(request,'login.html')
#allocation page
@login_required(login_url='login')
def allocations(request):
    print(request.user)
    return render(request,'HOD/allocations.html')

#allocate facultes
@login_required(login_url='login')
def tutor_allocation(request):
    user=User.objects.get(username=request.user)
    id=user.id
    hod=Hod.objects.get(id=id)
    dept_name=hod.hod_dept_name
    #print(dept_name)
    teacher=Teacher.objects.filter(teach_dept_name=dept_name)
    return render(request,'HOD/Allocations/Tutor/tutor_allocate.html',{'teacher':teacher})
#save to db
def tutor_allocating(request):
    if request.method=='POST':
        batch=request.POST['batch']
        tutor=request.POST['tutor']
        date=request.POST['date']
        dept_name=request.POST['dept_name']
        subject=request.POST['subject']
        if Tutor_allocation.objects.filter(batch=batch).exists():
            print('Already allocated')
            messages.error(request, 'already allocated')
            return redirect('class_tutors')
        else:
            #hod_id=request.user.id
            #teach=User.objects.get(username=tutor)
            #teach_id=teach.id
            if Tutor_allocation.objects.filter(tutor=tutor).exists():
                messages.error(request, 'already allocated')
                return redirect('class_tutors')
            else:
                print('**')
                class_tutor=Tutor_allocation(batch=batch,tutor=tutor,date=date,dept_name=dept_name,subject=subject)
                class_tutor.save()  
                print('SAVED')     
                return redirect('class_tutors')
            return redirect('class_tutors')
def class_tutors(request):
    tutors=Tutor_allocation.objects.all()
    return render(request,'HOD/Allocations/Tutor/show_class_tutors.html',{'tutors':tutors})
def subject_alloc(request):
    user=User.objects.get(username=request.user)
    id=user.id
    hod=Hod.objects.get(id=id)
    dept_name=hod.hod_dept_name
    #print(dept_name)
    teacher=Teacher.objects.filter(teach_dept_name=dept_name)
    print('subject****')
    return render(request,'HOD/Allocations/Subject/subject_allocations.html',{'teacher':teacher,'dept_name':dept_name})

def subject_allocation(request):
    if request.method=='POST':
        batch=request.POST['batch']
        tutor=request.POST['tutor']
        date=request.POST['date']
        dept_name=request.POST['dept_name']
        subject=request.POST['subject']        
        if Subject_allocation.objects.filter(subject=subject,batch=batch).exists():
            messages.error(request, 'already allocated')
            return redirect('subject_tutors')
        else:
            print('**')
            subject_tutor=Subject_allocation(batch=batch,tutor=tutor,date=date,dept_name=dept_name,subject=subject)
            subject_tutor.save()  
            print('SAVED')     
            return redirect('subject_tutors')
    return redirect('class_tutors')
def subject_tutors(request):
    tutors=Subject_allocation.objects.all()
    return render(request,'HOD/Allocations/Subject/show_subject_allocations.html',{'tutors':tutors})
def time_table(request):
    user=User.objects.get(username=request.user.username)
    id=user.id
    hod=Hod.objects.get(id=id)
    dept_name=hod.hod_dept_name
    teacher=Teacher.objects.filter(teach_dept_name=dept_name)
    return render(request,'HOD/Allocations/Time_Table/time_table.html',{'teacher':teacher,'dept_name':dept_name})
def time_table_coordinator(request):
    if request.method=='POST':
        username=request.POST['tutor']
        date=request.POST['date']
        dept_name=request.POST['dept_name']
        if Time_table_coordinator.objects.filter(dept_name=dept_name).exists():
            messages.error(request,'Already allocated')
            return redirect('show_time_table')
        else:
            time_table_coordinators=Time_table_coordinator(username=username,date=date,dept_name=dept_name)
            time_table_coordinators.save()
            print('SAVED')
            messages.info(request,'Time table coordinator is assigned')
            return redirect('show_time_table')
def show_time_table(request):
    coordinator=Time_table_coordinator.objects.all()
    return render(request,'HOD/Allocations/Time_Table/show_time_table.html',{'coordinator':coordinator})
def placement(request):
    user=User.objects.get(id=request.user.id)
    user_id=user.id
    hod=Hod.objects.get(id=user_id)
    dept_name=hod.hod_dept_name
    coordinator=Teacher.objects.filter(teach_dept_name=dept_name)
    return render(request,'HOD/Allocations/Placement/placements.html',{'coordinator':coordinator,'dept_name':dept_name})
def placement_coordinator(request):
    if request.method=='POST':
        username=request.POST['tutor']
        date=request.POST['date']
        dept_name=request.POST['dept_name']
        if Placement_coordinator.objects.filter(dept_name=dept_name).exists():
            messages.info(request,'Already allocated')
            return redirect('show_placement_coordinators')
        else:
            Placement_coordinators=Placement_coordinator(username=username,date=date,dept_name=dept_name)
            Placement_coordinators.save()
            print('SAVED')
            messages.info(request,'placement coordinator assigned')
            return redirect('show_placement_coordinators')
def show_placement_coordinators(request):
    coordinators=Placement_coordinator.objects.all()
    return render(request,'HOD/Allocations/Placement/show_placements.html',{'coordinator':coordinators})
        

