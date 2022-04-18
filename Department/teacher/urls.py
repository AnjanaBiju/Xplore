from django.urls import path
from teacher import views

urlpatterns = [
    path('teacher',views.teacher,name='teacher'),
    path('teacher_register',views.teacher_register,name='teacher_register'),
    path('welcome',views.welcome,name='welcome'),
    path('attendance_marking',views.attendance_marking,name='attendance_marking'),
    path('placement_notification',views.placement_notification,name='placement_notification'),
    path('subject_alloc_notification',views.subject_alloc_notification,name='subject_alloc_notification'),
    path('exam_notifications',views.exam_notifications,name='exam_notifications'),
    path('time_table_notifications',views.time_table_notifications,name='time_table_notifications'),
    path('tutor_notifications',views.tutor_notifications,name='tutor_notifications'),
    path('student_list',views.student_list,name='student_list'),
    path('placement_welcome',views.placement_welcome,name='placement_welcome'),
    path('questions',views.questions,name='questions'),
    path('add_questions',views.add_questions,name='add_questions'),
    path('show_questions',views.show_questions,name='show_questions'),
    path('time_table_welcome',views.time_table_welcome,name='time_table_welcome'),
    path('time_table_generation',views.time_table_generation,name='time_table_generation'),
    path('attendance_marking',views.attendance_marking,name='attendance_marking'),
]
