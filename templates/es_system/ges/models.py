from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime
# Create your models here.
     
class v_buildings(models.Model):
    bino_nomi=models.CharField(max_length=266)
    oxirgi_audit = models.DateField(default=now)
    bino_turi = models.CharField(max_length=266)
    
    umumiy_maydoni = models.FloatField()
    isitish_hajmi = models.FloatField() 
    isitish_maydoni = models.FloatField()    
    sovutiladigan_maydon = models.FloatField() 
    foydali_maydon = models.FloatField() 
    koridor = models.FloatField()     
    
    etajlar_soni = models.FloatField() 
    xonalar_soni = models.FloatField() 
    xodimlar_soni = models.FloatField() 
    ish_soatlari = models.FloatField() 
    
    yillik_elektr_sarfi = models.FloatField() 
    yillik_gaz_sarfi = models.FloatField() 
    yillik_issiq_suv_sarfi = models.FloatField() 
    yillik_bug_sarfi = models.FloatField() 
    yillik_komir_sarfi = models.FloatField() 
    yillik_neft_mahsulotlari_sarfi = models.FloatField() 
    
    
        
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.bino_nomi
    
    class Meta:
        ordering: ['-oxirgi_audit']

class v_parameters(models.Model):
    nomi=models.CharField(max_length=266)
    sana = models.DateField()    
    #ishlab chiqarish    
    aktiv_elektr_energiya = models.FloatField()    
    reaktiv_elektr_energiya = models.FloatField() 
    
    #qayta tiklanuvchi manbalardan ishlab chiqarish
    qtm_energiya = models.FloatField()        
    
    #Suv haqida
    suv_oqimi = models.FloatField() 
    trubina_suv_sarfi = models.FloatField()
    salt_suv_sarfi = models.FloatField()  
    suv_omboridagi_suv_hajmi = models.FloatField()  
    
    #boshqa ehtiyoj uchun
    xususiy_elektr_energiya = models.FloatField() 
    benzin = models.FloatField() 
    dizel = models.FloatField()     
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        ordering: ['sana']

class new_periodical(models.Model):
    hisobot_nomi=models.CharField(max_length=266)
    hisobot_sanasi = models.DateField()
    
    sum=0    
    for ee in v_parameters.objects.all():
        sum=sum+ee.aktiv_elektr_energiya
    jami_ee=sum
    
    sum=0 
    for ee in v_parameters.objects.all():
        sum=sum+ee.reaktiv_elektr_energiya
    jami_re=sum
    
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.hisobot_nomi
    
    class Meta:
        ordering: ['hisobot_sanasi']