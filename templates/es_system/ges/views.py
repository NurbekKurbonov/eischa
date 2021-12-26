from django.contrib import messages
from django.shortcuts import render, redirect
from .models import v_buildings, v_parameters, new_periodical

from django.contrib import messages
def index(request):
    return render(request, 'ges/index.html')

#profilda ishlash ************************************

def profile(request):
    return render(request, 'ges/profile.html')

#*****************************************************

#bino inshootlari ma'lumotini kiritish****************
from django.core.paginator import Paginator

def input_buildings(request):    
    buildings = v_buildings.objects.filter(owner=request.user)
    
    context = {
        'buildings': buildings,     
        
    }    
    return render(request, 'ges/input_buildings.html', context)

#*****************************************************


def add_buildings(request):    
    context = {             
        'values': request.POST
    }
    
    if request.method == 'GET':
        return render(request, 'ges/add_buildings.html', context)

    if request.method == 'POST':        
        bino_nomi = request.POST['bino_nomi']
        oxirgi_audit = request.POST['oxirgi_audit']
        bino_turi = request.POST['bino_turi']
        umumiy_maydoni = request.POST['umumiy_maydoni']
        isitish_hajmi = request.POST['isitish_hajmi']
        isitish_maydoni = request.POST['isitish_maydoni']
        sovutiladigan_maydon = request.POST['sovutiladigan_maydon']
        foydali_maydon = request.POST['foydali_maydon']
        koridor = request.POST['koridor']    
        
        etajlar_soni = request.POST['etajlar_soni']
        xonalar_soni = request.POST['xonalar_soni']
        xodimlar_soni = request.POST['xodimlar_soni']
        ish_soatlari = request.POST['ish_soatlari']
        
        yillik_elektr_sarfi = request.POST['yillik_elektr_sarfi']
        yillik_gaz_sarfi =  request.POST['yillik_gaz_sarfi']
        yillik_issiq_suv_sarfi = request.POST['yillik_issiq_suv_sarfi']
        yillik_bug_sarfi = request.POST['yillik_bug_sarfi']
        yillik_komir_sarfi = request.POST['yillik_komir_sarfi']
        yillik_neft_mahsulotlari_sarfi = request.POST['yillik_neft_mahsulotlari_sarfi']
        
        if not bino_nomi :
            messages.error(request, 'Bino nomini kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not oxirgi_audit :
            messages.error(request, 'Oxirgi audit sanasini kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not bino_turi :
            messages.error(request, 'Bino turini kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not umumiy_maydoni :
            messages.error(request, 'Umumiy maydonni kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not isitish_hajmi :
            messages.error(request, 'Isitish hajmini kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not isitish_maydoni :
            messages.error(request, 'Isitish maydonini kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not foydali_maydon :
            messages.error(request, 'Foydali maydonni kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not koridor :
            messages.error(request, 'Koridor maydonini kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not etajlar_soni :
            messages.error(request, 'Etajlar sonini kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not xodimlar_soni :
            messages.error(request, 'Xodimlar sonini kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not ish_soatlari :
            messages.error(request, 'Ish soatlarini kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not yillik_elektr_sarfi :
            messages.error(request, 'Yillik elektr sarfini kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not yillik_gaz_sarfi :
            messages.error(request, 'Yillik gaz sarfini kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not yillik_bug_sarfi :
            messages.error(request, 'Yillik gaz sarfini kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not yillik_komir_sarfi :
            messages.error(request, 'Yillik ko`mir sarfi ni kiriting')
            return render(request, 'ges/add_buildings.html', context)
        if not yillik_neft_mahsulotlari_sarfi :
            messages.error(request, 'Yillik neft mahsulotlari sarfini kiriting')
            return render(request, 'ges/add_buildings.html', context)  
        if not yillik_issiq_suv_sarfi :
            messages.error(request, 'Yillik issiq suv sarfini kiriting')
            return render(request, 'ges/add_buildings.html', context)           
        
        v_buildings.objects.create(owner=request.user, bino_nomi =bino_nomi , oxirgi_audit =oxirgi_audit , bino_turi =bino_turi , umumiy_maydoni =umumiy_maydoni , isitish_hajmi =isitish_hajmi , isitish_maydoni =isitish_maydoni , sovutiladigan_maydon =sovutiladigan_maydon , foydali_maydon =foydali_maydon , koridor =koridor ,
                                    etajlar_soni =etajlar_soni , xonalar_soni =xonalar_soni , xodimlar_soni =xodimlar_soni , ish_soatlari =ish_soatlari , yillik_elektr_sarfi =yillik_elektr_sarfi ,yillik_gaz_sarfi=yillik_gaz_sarfi, yillik_issiq_suv_sarfi =yillik_issiq_suv_sarfi , yillik_komir_sarfi=yillik_komir_sarfi,
                                    yillik_bug_sarfi =yillik_bug_sarfi, yillik_neft_mahsulotlari_sarfi=yillik_neft_mahsulotlari_sarfi)        
        messages.success(request, 'Yangi bino muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('ges_inbuild')

#*****************************************************

#Davriy ma'lumotlar listi****************

def input_periodical(request):
    parameters = v_parameters.objects.filter(owner=request.user)
    
    context = {
        'parameters': parameters,     
        
    } 
    return render(request, 'ges/input_periodical.html', context)

#**********************************************
#Davriy ma'lumotlarni kiritish****************

def add_periodical(request):
    context = {             
        'values_p': request.POST
    }
    
    if request.method == 'GET':
        return render(request, 'ges/add_periodical.html',context)
    
    if request.method == 'POST':        
        nomi = request.POST['nomi']
        sana = request.POST['sana']
        aktiv_elektr_energiya = request.POST['aktiv_elektr_energiya']
        reaktiv_elektr_energiya = request.POST['reaktiv_elektr_energiya']
        
        qtm_energiya = request.POST['qtm_energiya']
        suv_oqimi = request.POST['suv_oqimi']
        trubina_suv_sarfi = request.POST['trubina_suv_sarfi']
        salt_suv_sarfi = request.POST['salt_suv_sarfi']
        suv_omboridagi_suv_hajmi = request.POST['suv_omboridagi_suv_hajmi']    
        
        xususiy_elektr_energiya = request.POST['xususiy_elektr_energiya']
        benzin = request.POST['benzin']
        dizel= request.POST['dizel'] 
        
        if not nomi :
            messages.error(request, 'Hisobot nomini kiriting')
            return render(request, 'ges/add_periodical.html', context)
        if not sana :
            messages.error(request, 'sanani belgilang')
            return render(request, 'ges/add_periodical.html', context)
        if not aktiv_elektr_energiya :
            messages.error(request, 'Aktiv elektr energiyani kiriting')
            return render(request, 'ges/add_periodical.html', context)
        if not reaktiv_elektr_energiya :
            messages.error(request, 'Reaktiv elektr energiyani kiriting')
            return render(request, 'ges/add_periodical.html', context)
        if not qtm_energiya :
            messages.error(request, 'Qayta tiklanuvchi manbalardan olingan energiya miqdorini kiriting')
            return render(request, 'ges/add_periodical.html', context)
        if not suv_oqimi :
            messages.error(request, 'Suv oqimini kiriting')
            return render(request, 'ges/add_periodical.html', context)
        if not trubina_suv_sarfi:
            messages.error(request, 'Turbinadagi suv sarfini kiriting')
            return render(request, 'ges/add_periodical.html', context)
        if not salt_suv_sarfi :
            messages.error(request, 'Salt oqizilgan suv sarfini kiriting')
            return render(request, 'ges/add_periodical.html', context)
        if not suv_omboridagi_suv_hajmi :
            messages.error(request, 'Suv omboridagi suv hajmini kiriting')
            return render(request, 'ges/add_periodical.html', context)
        if not xususiy_elektr_energiya :
            messages.error(request, 'O`z ehtiyoji uchun sarflangan elektr energiya miqdorini kiriting')
            return render(request, 'ges/add_periodical.html', context)
        if not benzin :
            messages.error(request, 'Benzin miqdorini kiriting')
            return render(request, 'ges/add_periodical.html', context)
        if not dizel :
            messages.error(request, 'Dizel miqdorini kiriting')
            return render(request, 'ges/add_periodical.html', context)        
        
        v_parameters.objects.create(owner=request.user, nomi=nomi, sana =sana , aktiv_elektr_energiya =aktiv_elektr_energiya , reaktiv_elektr_energiya =reaktiv_elektr_energiya , 
                                    qtm_energiya =qtm_energiya , suv_oqimi =suv_oqimi , trubina_suv_sarfi =trubina_suv_sarfi , salt_suv_sarfi =salt_suv_sarfi , 
                                    suv_omboridagi_suv_hajmi =suv_omboridagi_suv_hajmi , xususiy_elektr_energiya =xususiy_elektr_energiya , benzin =benzin , dizel =dizel)        
        messages.success(request, 'Hisobot muvofaqqiyatli yuborildi! Rahmat! Charchamang! :)')
        return redirect('ges_inperiodical')
#**********************************************
#Davriy hisobotlar****************************

def periodical(request):
    p_objects = new_periodical.objects.all()
    context = {
        'p_objects': p_objects
    }
    return render(request, 'ges/report/periodical.html', context)

def new_perodical(request):
    n_objects=v_parameters.objects.all()    
    
    context = {
        'n_objects': n_objects,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'ges/report/periodical_filter.html',context)
    
    if request.method == 'POST':
        hisobot_nomi = request.POST['hisobot_nomi']
        hisobot_sanasi = request.POST['hisobot_sanasi']
        
        new_periodical.objects.create(owner=request.user, hisobot_nomi=hisobot_nomi, hisobot_sanasi=hisobot_sanasi)
        messages.success(request, 'Hisobot muvofaqqiyatli yuborildi! Rahmat! Charchamang! :)')
        return redirect('ges_result_periodical')        
    
# Davriy hisobotlarni shakllantirish
def result_perodical(request):
    r_objects=new_periodical.objects.last()
    all = v_parameters.objects.all()
    context = {
        'r_objects': r_objects,
        'all':all
    }
    return render(request, 'ges/report/results/result_periodical.html', context)    

def result_perodical2(request):
    r_objects=new_periodical.objects.last()
    all = v_parameters.objects.all()
    context = {
        'r_objects': r_objects,
        'all':all
    }
    return render(request, 'ges/report/results/result_periodical2.html', context)    
   
def result_perodical3(request):
    r_objects=new_periodical.objects.last()
    all = v_parameters.objects.all()
    context = {
        'r_objects': r_objects,
        'all':all
    }
    return render(request, 'ges/report/results/result_periodical3.html', context)    

def result_perodical4(request):
    r_objects=new_periodical.objects.last()
    all = v_parameters.objects.all()
    context = {
        'r_objects': r_objects,
        'all':all
    }
    return render(request, 'ges/report/results/result_periodical4.html', context)    

#**********************************************

#Bashoratlash**********************************

def forecasting(request):
    return render(request, 'ges/report/forecasting.html')

#**********************************************

#Balance **************************************

def balance(request):
    return render(request, 'ges/report/balance.html')

#**********************************************
