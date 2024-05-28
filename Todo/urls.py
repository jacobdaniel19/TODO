"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from todo_app.views import Registration,Sign_in,Add_task,Delete_task,Edit_task,Sign_out,User_del

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('create/',Registration.as_view()),
    path('login/',Sign_in.as_view(),name="signin"),
    path('index/',Add_task.as_view(),name="index"),
    path('delete/<int:pk>',Delete_task.as_view(),name="delete"),
    path('index/update/<int:pk>',Edit_task.as_view(),name="update"),
    path('logout/',Sign_out.as_view(),name="logout"), 
    path('del_user/<int:pk>',User_del.as_view(),name="del"),
]
