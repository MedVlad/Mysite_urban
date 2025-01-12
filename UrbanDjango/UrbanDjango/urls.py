"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from lib2to3.fixes.fix_input import context

from django.contrib import admin
from django.urls import path
from task2.views import index_function, Index_class
#from task3.views import index,market,cart
from task4.views import index,market,cart
from task5.views import sign_up_by_html,sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', index_function),
    path('class/', Index_class.as_view()),
    path('index/',index),
    path('market/', market),
    path('cart/', cart),
    #path('',index),
    path('',sign_up_by_html),
    path('django_sign_up/', sign_up_by_django)
]
