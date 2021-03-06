# Generated by Django 4.0.2 on 2022-04-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Subject', models.CharField(max_length=200)),
                ('Question', models.CharField(max_length=200)),
                ('Dept_name', models.CharField(max_length=200)),
                ('OptionA', models.CharField(max_length=200)),
                ('OptionB', models.CharField(max_length=200)),
                ('OptionC', models.CharField(max_length=200)),
                ('OptionD', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
                ('Level', models.CharField(max_length=200)),
                ('Score', models.IntegerField()),
            ],
        ),
    ]
