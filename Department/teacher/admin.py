from django.contrib import admin


from teacher.models import Subjects, Teacher, Questions

# Register your models here.
admin.site.register(Subjects)
admin.site.register(Teacher)
admin.site.register(Questions)