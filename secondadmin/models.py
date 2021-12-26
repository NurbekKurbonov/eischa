from django.db import models
from django.contrib.auth.models import User

class Davlatlar(models.Model):
    davlat_kodi = models.IntegerField('Davlat kodi')
    davlat_nomi = models.CharField(max_length=100)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.davlat_nomi
    
    class Meta:
        ordering: ['-davlat_kodi']
        verbose_name_plural = '01_Davlatlar'
    

class Viloyat(models.Model):
    viloyat_davlati = models.CharField('Viloyat joylashgan davlat', max_length=100)
    viloyat_kodi = models.IntegerField('Viloyat kodi')
    viloyat_nomi = models.CharField('Viloyat nomi', max_length=100)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.viloyat_nomi
    
    class Meta:
        ordering: ['-viloyat_kodi']
        verbose_name_plural = '02_Viloyatlar'

class Tuman(models.Model):
    tuman_davlati = models.CharField('Tuman/shahar joylashgan davlat', max_length=100)
    tuman_viloyati = models.CharField('Tuman/shahar joylashgan viloyat', max_length=100)
    tuman_kodi = models.IntegerField('Tuman/shahar kodi')
    tuman_nomi = models.CharField('Tuman/shahar nomi', max_length=100)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tuman_nomi
    
    class Meta:
        ordering: ['-tuman_kodi']
        verbose_name_plural = '03_Tumanlar'

#*************************__________IFTUM__________**********************

class IFTUM(models.Model):
    bolim = models.CharField('Bo`lim', max_length=2)
    bob = models.IntegerField('Bob')
    guruh = models.IntegerField('Guruh')
    sinf = models.IntegerField('Sinf')
    tartib = models.IntegerField('Tartib')
    nomi = models.TextField('IFTUM nomi', unique=True)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        verbose_name_plural = '04_IFTUM kodi'
    