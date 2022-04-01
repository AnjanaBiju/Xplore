from django.shortcuts import render
from django.contrib.auth.models import User, auth
#from Department.teacher.models import Teacher
from django.contrib.auth.decorators import login_required

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
   # for i in teacher:
       # print(teacher.teach_dept_name)
    #print(teacher.id.username)
    return render(request,'HOD/tutor_allocate.html',{'teacher':teacher})

