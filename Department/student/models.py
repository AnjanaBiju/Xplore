from operator import mod
from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Student(models.Model):
    stud_id=models.AutoField(primary_key=True,null=False)
    id=models.ForeignKey(User,on_delete=models.CASCADE)
    stud_dept_name=models.CharField(max_length=25)
    stud_branch=models.IntegerField()
    stud_dob=models.DateField()
    stud_phone=models.IntegerField()
    stud_image=models.FileField(upload_to='images')