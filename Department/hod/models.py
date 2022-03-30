from platform import mac_ver
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Hod(models.Model):
    hod_id=models.AutoField(primary_key=True)
    id=models.ForeignKey(User,on_delete=models.CASCADE)
    hod_dept_name=models.CharField(max_length=75)
    hod_qualification=models.CharField(max_length=100)
    hod_group=models.IntegerField()
    hod_dob=models.DateField()
    hod_phone=models.IntegerField()
    hod_image=models.FileField()