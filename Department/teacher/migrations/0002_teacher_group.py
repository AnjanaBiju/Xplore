# Generated by Django 4.0.2 on 2022-03-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='group',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
