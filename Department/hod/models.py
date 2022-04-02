from platform import mac_ver
from pyexpat import model
from telnetlib import Telnet
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from teacher.models import Teacher
# Create your models here.
class Hod(models.Model):
    hod_id=models.AutoField(primary_key=True)
    id=models.ForeignKey(User,on_delete=models.CASCADE)
    hod_dept_name=models.CharField(max_length=75)
    hod_qualification=models.CharField(max_length=100)
    hod_group=models.IntegerField()
    hod_dob=models.DateField()
    hod_phone=models.IntegerField()
    hod_image=models.FileField(upload_to='images')
    def __str__(self):
        return self.user.username
class Tutor_allocation(models.Model):
    #hod_id=models.ForeignKey(Hod,on_delete=models.CASCADE)
    #teach_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    tutor=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    dept_name=models.CharField(max_length=200)
    batch=models.CharField(max_length=200)
    date=models.DateField()
class Subject_allocation(models.Model):
    tutor=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    dept_name=models.CharField(max_length=200)
    batch=models.CharField(max_length=200)
    date=models.DateField()
class Time_table_coordinator(models.Model):
    username=models.CharField(max_length=200)
    date=models.DateField()
    dept_name=models.CharField(max_length=200)
class Placement_coordinator(models.Model):
    username=models.CharField(max_length=200)
    dept_name=models.CharField(max_length=200)
    date=models.DateField()
class Exam_coordinator(models.Model):
    username=models.CharField(max_length=200)
    dept_name=models.CharField(max_length=200)
    date=models.DateField()


