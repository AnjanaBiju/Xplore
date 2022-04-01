from django.urls import path
from hod import views

urlpatterns = [
    path('hod',views.hod,name='hod'),
    path('hod_register',views.hod_register,name='hod_register'),
    path('/welcomes/allocations',views.allocations,name='welcomes-allocations'),
    path('/welcomes/tutor_allocation',views.tutor_allocation,name='welcomes-tutor_allocation')
    ]