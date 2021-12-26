
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    
    #path('profile', views.profile, name='ges_profile'),
    #path('ges_inbuild', views.input_buildings, name='ges_inbuild'),
    #path('ges_addbuild', views.add_buildings, name='ges_addbuild'),
    
    path('inperiodical', views.inperiodical, name='inperiodical'), 
    path('addperiodical', views.addperiodical, name='addperiodical'), 
       
    #path('ges_periodical', views.periodical, name='ges_periodical'), 
    #path('ges_new_perodical', views.new_perodical, name='ges_new_periodical'),
    #path('ges_result_periodical', views.result_perodical, name='ges_result_periodical'),
    #path('ges_result_periodical2', views.result_perodical2, name='ges_result_periodical2'),
    #path('ges_result_periodical3', views.result_perodical3, name='ges_result_periodical3'),
    #path('ges_result_periodical4', views.result_perodical4, name='ges_result_periodical4'),
    
    #path('ges_forecasting', views.forecasting, name='ges_forecasting'),    
    #path('ges_balance', views.balance, name='ges_balance'),  
]
