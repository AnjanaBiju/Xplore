# Generated by Django 4.0.2 on 2022-03-29 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hod',
            fields=[
                ('hod_id', models.AutoField(primary_key=True, serialize=False)),
                ('hod_dept_name', models.CharField(max_length=75)),
                ('hod_qualification', models.CharField(max_length=100)),
                ('hod_group', models.IntegerField()),
                ('hod_dob', models.DateField()),
                ('hod_phone', models.IntegerField()),
                ('hod_image', models.FileField(upload_to='')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]