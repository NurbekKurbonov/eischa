
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('country', views.davlat, name='country'),
    path('addcountry', views.adddavlat, name='addcountry'),
    path('delcountry/<int:id>', views.del_davlat, name='delcountry'),
    path('editcountry/<int:id>', views.editdavlat, name='editcountry'),
    
    path('viloyat', views.viloyat, name='viloyat'),
    path('addviloyat', views.addviloyat, name='addviloyat'),
    path('delviloyat/<int:id>', views.del_viloyat, name='delviloyat'),
    path('editviloyat/<int:id>', views.editviloyat, name='editviloyat'),
    
    path('tuman', views.tuman, name='tuman'),
    path('addtuman', views.addtuman, name='addtuman'),
    path('deltuman/<int:id>', views.del_tuman, name='deltuman'),
    path('edittuman/<int:id>', views.edittuman, name='edittuman'),

    path('oked', views.oked, name='oked'),
    path('addoked', views.addoked, name='addoked'),
    path('deloked/<int:id>', views.del_oked, name='deloked'),
    path('editoked/<int:id>', views.editoked, name='editoked'),

    path('birlik', views.kattalik, name='birlik'),
]
