"""Department URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django import views
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Department import views
#import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('cards_register',views.card_register,name='card_register'),
    path('login_user',views.login_user,name='login_user'),
    path('',include('student.urls')),
    path('',include('teacher.urls')),
    path('',include('hod.urls')),
    path('welcomes',views.welcomes,name='welcomes')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
