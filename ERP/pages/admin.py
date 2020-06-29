from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Page)

#Configuracion de panel
title = "ERP"
subtitle = "Panel de gestion" 

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle