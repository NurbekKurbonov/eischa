from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import IFTUM, Davlatlar, Tuman, Viloyat

def index(request):
    return render(request, 'secondadmin/index.html')

def davlat(request):
    davlatlar = Davlatlar.objects.filter(owner=request.user)
    
    context = {
        'davlatlar': davlatlar,
    } 
    return render(request, 'secondadmin/parts/01_country.html', context)

def adddavlat(request):
    context = {             
        'countries': request.POST
    }
    
    if request.method == 'GET':
        return render(request, 'secondadmin/parts/01_1_addcountry.html', context)
            
    if request.method == 'POST':        
        davlat_kodi = request.POST['davlat_kodi']
        davlat_nomi = request.POST['davlat_nomi']        
        
        Davlatlar.objects.create(owner=request.user, davlat_kodi=davlat_kodi, davlat_nomi=davlat_nomi )        
        messages.success(request, 'Yangi davlat muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('country')

def editdavlat(request, id):
       
    davlat = Davlatlar.objects.get(pk=id)
    
    context = {
        'davlat': davlat,
        'values': davlat,
    } 
    
    if request.method == 'GET':  
        return render(request, 'secondadmin/parts/01_2_editcountry.html', context)
    
    if request.method == 'POST':  
        davlat_kodi = request.POST['davlat_kodi']
        davlat_nomi = request.POST['davlat_nomi'] 
        
        davlat.owner=request.user
        davlat.davlat_kodi=davlat_kodi
        davlat.davlat_nomi=davlat_nomi
        
        davlat.save()
        messages.success(request, 'Davlat muvofaqqiyatli yangilandi!')
        
        return redirect('country')

def del_davlat(request, id):
    davlat = Davlatlar.objects.get(pk=id)
    davlat.delete()
    messages.success(request, 'Davlat o`chirildi')
    return redirect('country')

#viloyat ***************************-------------------------**********************
def viloyat(request):
    viloyat = Viloyat.objects.all()
    
    context = {
        'viloyat': viloyat
    }
    return render(request, 'secondadmin/parts/02_viloyat.html', context)

def addviloyat(request):
    davlatlar = Davlatlar.objects.all()
    
    context = {          
        'davlatlar': davlatlar,  
        'values': request.POST          
        
    }
    
    if request.method == 'GET':
        return render(request, 'secondadmin/parts/02_1_addviloyat.html', context)
            
    if request.method == 'POST':        
        viloyat_davlati = request.POST['viloyat_davlati']
        viloyat_kodi = request.POST['viloyat_kodi']
        viloyat_nomi = request.POST['viloyat_nomi']           
        
        Viloyat.objects.create(owner=request.user, viloyat_davlati=viloyat_davlati, viloyat_kodi=viloyat_kodi, viloyat_nomi=viloyat_nomi)        
        messages.success(request, 'Yangi viloyat muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('viloyat')
    
def editviloyat(request, id):
    davlatlar = Davlatlar.objects.all()   
    viloyat = Viloyat.objects.get(pk=id)
    
    context = {
        'davlatlar': davlatlar, 
        'viloyat': viloyat,
        'values': viloyat
    } 
    
    if request.method == 'GET':  
        return render(request, 'secondadmin/parts/02_2_editviloyat.html', context)
    
    if request.method == 'POST':  
        viloyat_davlati = request.POST['viloyat_davlati']
        viloyat_kodi = request.POST['viloyat_kodi']
        viloyat_nomi = request.POST['viloyat_nomi'] 
        
        viloyat.owner=request.user
        viloyat.viloyat_davlati=viloyat_davlati
        viloyat.viloyat_nomi=viloyat_nomi
        
        viloyat.save()
        messages.success(request, 'Davlat muvofaqqiyatli yangilandi!')
        
        return redirect('viloyat')

def del_viloyat(request, id):
    yoqol = Viloyat.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'Viloyat o`chirildi')
    return redirect('viloyat')

#tuman ***************************-------------------------**********************
def tuman(request):
    tuman = Tuman.objects.all()
    
    context = {
        'tuman': tuman
    }
    return render(request, 'secondadmin/parts/03_tuman.html', context)

def addtuman(request):    
    viloyatlar = Viloyat.objects.all()
    davlatlar = Davlatlar.objects.all()   
    
    context = {    
        'davlatlar': davlatlar,           
        'viloyatlar': viloyatlar,
        'values': request.POST          
        
    }
    
    if request.method == 'GET':
        return render(request, 'secondadmin/parts/03_1_addtuman.html', context)
            
    if request.method == 'POST':  
        tuman_davlati = request.POST['tuman_davlati']
        tuman_viloyati = request.POST['tuman_viloyati']
        tuman_kodi = request.POST['tuman_kodi']        
        tuman_nomi = request.POST['tuman_nomi']
        
        Tuman.objects.create(owner=request.user, tuman_davlati =tuman_davlati, tuman_viloyati = tuman_viloyati, tuman_kodi = tuman_kodi, tuman_nomi = tuman_nomi)
        messages.success(request, 'Yangi tuman muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('tuman')
    
def edittuman(request, id):   
    viloyatlar = Viloyat.objects.all()
    davlatlar = Davlatlar.objects.all()       
    tuman = Tuman.objects.get(pk=id)
    context = {        
        'davlatlar': davlatlar,
        'viloyatlar': viloyatlar,
        'tuman': tuman,
        'values': tuman
    } 
    
    if request.method == 'GET':  
        return render(request, 'secondadmin/parts/03_2_edittuman.html', context)
    
    if request.method == 'POST':  
        tuman_davlati = request.POST['viloyat_davlati']
        tuman_viloyati = request.POST['tuman_viloyati']
        tuman_kodi = request.POST['tuman_kodi']        
        tuman_nomi = request.POST['tuman_nomi']
        
        tuman.owner=request.user
        tuman.tuman_davlati=tuman_davlati
        tuman.tuman_viloyati = tuman_viloyati, 
        tuman.tuman_kodi = tuman_kodi, 
        tuman.tuman_nomi = tuman_nomi
        
        
        tuman.save()
        messages.success(request, 'Tuman muvofaqqiyatli yangilandi!')
        
        return redirect('tuman')

def del_tuman(request, id):
    yoqol = Tuman.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'Tuman o`chirildi')
    return redirect('tuman')

#*****************_____________OKED______________**********************

def oked(request):
    iftum = IFTUM.objects.all()
    context = {
        'iftum': iftum
    }
    return render(request, 'secondadmin/kod/01_IFTUM.html', context)

def addoked(request):    
    bolimlist = ["A", "B", "C", "D","E", "F","G", "H","I", "J","K", "L","M", "N","O", "P",]    
    context = {    
        'values': request.POST,
        'bolimlist': bolimlist                  
    }
    
    if request.method == 'GET':
        return render(request, 'secondadmin/kod/01_1_addiftum.html', context)
            
    if request.method == 'POST':  
        bolim = request.POST['bolim']
        bob = request.POST['bob']
        guruh = request.POST['guruh']
        sinf = request.POST['sinf']
        tartib = request.POST['tartib']
        nomi = request.POST['nomi']
        
        IFTUM.objects.create(owner=request.user, bolim= bolim, bob= bob, guruh= guruh, sinf= sinf, tartib= tartib, nomi=nomi)
        messages.success(request, 'Yangi IFTUM kodi muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('oked')

def editoked(request, id): 
    bolimlist = ["A", "B", "C", "D","E", "F","G", "H","I", "J","K", "L","M", "N","O", "P",]    
    iftum = IFTUM.objects.get(pk=id)
    context = {  
        'bolimlist':bolimlist,
        'iftum': iftum,        
        'values': iftum
    } 
    
    if request.method == 'GET':  
        return render(request, 'secondadmin/kod/01_2_editiftum.html', context)
    
    if request.method == 'POST':  
        bolim = request.POST['bolim']
        bob = request.POST['bob']
        guruh = request.POST['guruh']
        sinf = request.POST['sinf']
        tartib = request.POST['tartib']
        nomi = request.POST['nomi']
        
        iftum.bolim = bolim
        iftum.bob = bob
        iftum.guruh = guruh
        iftum.sinf = sinf
        iftum.tartib = tartib
        iftum.nomi =nomi
        
        iftum.owner=request.user
        
        iftum.save()
        messages.success(request, 'IFTUM kodi muvofaqqiyatli yangilandi!')
        
        return redirect('tuman')

def del_oked(request, id):
    yoqol = IFTUM.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'IFTUM kodi muvofaqqiyatli o`chirildi')
    return redirect('oked')

#**************____birlik_kiritish____****************

def kattalik(request):
    return render(request, 'secondadmin/kattalik/01_kattalik.html')
