# Generated by Django 4.0.2 on 2022-04-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_time_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internal_exams',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=200)),
                ('batch', models.CharField(max_length=200)),
                ('dept', models.CharField(max_length=200)),
                ('subject1', models.CharField(max_length=200)),
                ('subject2', models.CharField(max_length=200)),
                ('subject3', models.CharField(max_length=200)),
                ('subject4', models.CharField(max_length=200)),
                ('subject5', models.CharField(max_length=200)),
                ('subject6', models.CharField(max_length=200)),
                ('subject7', models.CharField(max_length=200)),
                ('mark1', models.IntegerField()),
                ('mark2', models.IntegerField()),
                ('mark3', models.IntegerField()),
                ('mark4', models.IntegerField()),
                ('mark5', models.IntegerField()),
                ('mark6', models.IntegerField()),
                ('mark7', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('percentage', models.IntegerField()),
            ],
        ),
    ]
