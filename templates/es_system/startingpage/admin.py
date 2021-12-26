from django.contrib import admin

from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date', 'permalink')
    ordering = ('title',)
    search_files = ('title',)

admin.site.register(Page, PageAdmin)