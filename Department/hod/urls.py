from django.urls import path

from hod import views

urlpatterns = [
    path('hod',views.hod,name='hod'),
    path('hod_register',views.hod_register,name='hod_register'),
    path('/welcomes/allocations',views.allocations,name='welcomes-allocations'),
    path('/welcomes/tutor_allocation',views.tutor_allocation,name='welcomes-tutor_allocation'),
    path('/welcomes/tutor_allocating',views.tutor_allocating,name='welcomes-tutor_allocating'),
    path('/welcomes/class_tutors',views.class_tutors,name='class_tutors'),
    path('/welcomes/subject_tutors',views.subject_tutors,name='subject_tutors'),
    path('/welcomes/subject_allocation',views.subject_allocation,name='subject_allocation'),
    path('/welcomes/subject_alloc',views.subject_alloc,name='subject_alloc'),
    path('/welcomes/time_table',views.time_table,name='time_table'),
    path('/welcomes/time_table_coordinator',views.time_table_coordinator,name='time_table_coordinator'),
    path('/welcomes/show_time_table',views.show_time_table,name='show_time_table'),
    path('/welcomes/placement',views.placement,name='placement'),
    path('/welcomes/placement_coordinator',views.placement_coordinator,name='placement_coordinator'),
    path('/welcomes/show_placement_coordinators',views.show_placement_coordinators,name='show_placement_coordinators'),
    path('/welcomes/exam_coordinators',views.exam_coordinators,name='exam_coordinators'),
    path('/welcomes/exam_coordination',views.exam_coordination,name='exam_coordination'),
    path('/welcomes/show_exam_coordinators',views.show_exam_coordinators,name='show_exam_coordinators'),
    ]