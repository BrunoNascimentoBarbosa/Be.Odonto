from django.contrib import admin
from .models import paciente,consulta
from django.utils.html import format_html

 
#from CadastroDentistas.models import Dentista,Especialidades

from django.contrib.admin import AdminSite

 
#https://www.youtube.com/watch?v=LaF0PQdV1wI
class pacienteDisplay(admin.ModelAdmin):
    list_display = ('nome','dentista','Tem_Diabete','Tem_hipertencao', )
    #list_editable = ('tratamento',)     
    search_fields = ('nome',) #Busca por nome de parciente
    list_filter = ('dentista','diabetico','hipertenso') # Filtro
    
    def Tem_Diabete(self, obj):
        icone1 = '<img src="https://img.icons8.com/doodle/22/000000/diabetes.png"/>'
        icone2 = '<img src="https://img.icons8.com/windows/22/000000/diabetes.png"/>'
        img = ''
        print(icone1)
        print(obj.diabetico)
        if obj.diabetico == 'S':
            img = icone1
        elif obj.diabetico == 'N':
            img = icone2
            
         
        return format_html(f'<strong><p ">{img}</p></strong>')     

    def Tem_hipertencao(self, obj):
        icone1 = '<img src="https://img.icons8.com/color/22/000000/hypertension.png"/>'
        icone2 = '<img src="https://img.icons8.com/ios/22/000000/hypertension.png"/>'
        img = ''
        if obj.hipertenso == 'S':
            img = icone1
        elif obj.hipertenso == 'N':
            img = icone2

        return format_html(f'<strong><p ">{img}</p></strong>')         



admin.site.register(paciente, pacienteDisplay)
admin.site.register(consulta)
 
 
 