from django.contrib import admin
from .models import Page

# Register your models here.

#Cnfiguracion extra para el panel de admin.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content') #Buscador. MUY UTIL. los 2 parametros es en donde va a buscar lo insertado
    list_filter = ('visible',) #Es un filtro, MUY UTIL tambien
    list_display = ('title', 'visible', 'created_at') #Una forma de listarlo en las columnas
    ordering = ('-created_at',)

admin.site.register(Page, PageAdmin) #debo pasarle aqui las configuraciones!!

#Codifugracion del panel
title = "Django Project Adrian Farji"
subtitle = "Project Management"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle