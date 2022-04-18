from django.urls import path
from student import views

urlpatterns = [
    path('student',views.student,name='student'),
    path('student_register',views.student_register,name='student-register'),
    path('welcome',views.welcome,name='welcome'),
    path('mock_entrance',views.mock_entrance,name='mock_entrance'),
]
