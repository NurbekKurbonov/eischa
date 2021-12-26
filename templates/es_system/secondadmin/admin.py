from django.contrib import admin

from .models import Davlatlar, Viloyat, Tuman, IFTUM

class PageSADavlat(admin.ModelAdmin):
    list_display = ('davlat_kodi', 'davlat_nomi')
    ordering = ('davlat_kodi',)
    search_files = ('davlat_kodi','davlat_nomi')

admin.site.register(Davlatlar, PageSADavlat)

class PageSAViloyat(admin.ModelAdmin):
    list_display = ('viloyat_kodi', 'viloyat_nomi', 'viloyat_davlati')
    ordering = ('viloyat_kodi',)
    search_files = ('viloyat_kodi','viloyat_nomi')
    
admin.site.register(Viloyat, PageSAViloyat)

class PageSATuman(admin.ModelAdmin):
    list_display = ('tuman_kodi', 'tuman_nomi', 'tuman_viloyati', 'tuman_davlati')
    ordering = ('tuman_kodi',)
    search_files = ('tuman_kodi',' tuman_nomi')
    
admin.site.register(Tuman, PageSATuman)

class PageSAIFTUM(admin.ModelAdmin):
    list_display = ('bolim', 'bob', 'guruh', 'sinf','nomi')
    ordering = ('bolim', 'bob', 'guruh', 'sinf', 'nomi')
    search_files = ('bolim', 'bob', 'guruh', 'sinf', 'nomi')
    
admin.site.register(IFTUM, PageSAIFTUM)

