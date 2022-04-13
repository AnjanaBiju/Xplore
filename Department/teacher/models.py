from operator import mod
from optparse import Option
from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Teacher(models.Model):
    teach_id=models.AutoField(primary_key=True,null=False)
    id=models.ForeignKey(User,on_delete=models.CASCADE)
    teach_dept_name=models.CharField(max_length=25)
    teach_designation=models.CharField(max_length=100)
    teach_dob=models.DateField()
    teach_phone=models.IntegerField()
    teach_image=models.FileField(upload_to='images')
    group=models.IntegerField()
    #1 for teachers
    #0 for students
    #2 for hods
class Subjects(models.Model):
    sub_code=models.AutoField(primary_key=True)
    subject=models.CharField(max_length=200)
    dept_name=models.CharField(max_length=200)
    semester=models.IntegerField()
class Questions(models.Model):
    id=models.AutoField(primary_key=True)
    Subject=models.CharField(max_length=200)
    Question=models.CharField(max_length=200)
    Dept_name=models.CharField(max_length=200)
    OptionA=models.CharField(max_length=200)
    OptionB=models.CharField(max_length=200)
    OptionC=models.CharField(max_length=200)
    OptionD=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)
    Level=models.CharField(max_length=200)
    Score=models.IntegerField()