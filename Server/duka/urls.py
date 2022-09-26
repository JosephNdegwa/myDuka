from django.urls import path,include
from django.conf import settings

from duka import views

urlpatterns=[
    path('',views.welcome,name= 'welcome'),
    

]