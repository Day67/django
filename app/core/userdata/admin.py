from django.contrib import admin
from .models import Roles,DatosUser,Habilidades,Rates,DetaRoles
# Register your models here.
#Registro del modelo Rol
class RolModel(admin.ModelAdmin):
    list_display =["roleName"]
    list_display_links =["roleName"]
    list_filter = ["roleName"]
    class Meta:
        model=Roles
admin.site.register(Roles)
#Registro del modelo DatosUser
class DatosUserModel(admin.ModelAdmin):
    list_display =["nombreUser"]
    list_display_links =["nombreUser"]
    list_filter = ["nombreUser"]
    class Meta:
        model = DatosUser
admin.site.register(DatosUser)
#Registro del modelo Habilidades
class HabilidadesModel(admin.ModelAdmin):
    list_display =["nombreHabilidad"]
    list_display_links =["nombreHabilidad"]
    list_filter = ["nombreHabilidad"]
    class Meta:
        model =Habilidades
admin.site.register(Habilidades)
#Registro del modelo Rates
class RatesModel(admin.ModelAdmin):
    list_display =["Porcentaje"]
    list_display_links =["Porcentaje"]
    list_filter = ["Porcentaje"]
    class Meta:
        model= Rates
admin.site.register(Rates)
#Registro del modelo DetaRoles
class DetaRolesModel(admin.ModelAdmin):
    list_display =["EstadoRol"]
    list_display_links =["EstadoRol"]
    list_filter = ["EstadoRol"]
    class Meta:
        model= DetaRoles
admin.site.register(DetaRoles)