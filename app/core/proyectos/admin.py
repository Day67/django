from django.contrib import admin
from .models import TipoDocu,CategProye,Proyectos,Documentos
# Register your models here.
class TipoDocuModel(admin.ModelAdmin):
    list_display =["nombTiDoc"]
    list_display_links =["nombTiDoc"]
    list_filter = ["nombTiDoc"]
    class Meta:
        model=TipoDocu
admin.site.register(TipoDocu)
class CategProyeModel(admin.ModelAdmin):
    list_display =["lenguaje"]
    list_display_links =["lenguaje"]
    list_filter = ["lenguaje"]
    class Meta:
        model=CategProye
admin.site.register(CategProye)
class ProyectosModel(admin.ModelAdmin):
    list_display =["nombProye"]
    list_display_links =["nombProye"]
    list_filter = ["nombProye"]
    class Meta:
        model=Proyectos
admin.site.register(Proyectos)
class DocumentosModel(admin.ModelAdmin):
    list_display =["idTipoDocu"]
    list_display_links =["idTipoDocu"]
    list_filter = ["idTipoDocu"]
    class Meta:
        model=Documentos
admin.site.register(Documentos)
