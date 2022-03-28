from django.urls import path
from teacher import views

urlpatterns = [
    path('teacher',views.teacher,name='teacher'),
    path('teacher_register',views.teacher_register,name='teacher_register'),
    path('welcome',views.welcome,name='welcome'),
]
