import imp
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from duka import views

urlpatterns=[
    path('',views.welcome,name= 'welcome'),
    path('api/clothes/', views.ClothesList.as_view())
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)