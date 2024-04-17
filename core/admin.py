from django.contrib import admin
from core.models import Usuario,Deporte,Campeonato,Eventos,Equipos,Desafios,Rendimiento

class UsuariosAdmin(admin.ModelAdmin):
    list_display=("codigo","nombre","edad","sexo","tipo")

class DeporteAdmin(admin.ModelAdmin):
    list_display=("idDeporte","nombre_dep")

class CampeonatoAdmin(admin.ModelAdmin):
    list_display=("idCampeonato","nombre","tipo","idDeporte")

class EventosAdmin(admin.ModelAdmin):
    list_display=("nombre_ev","fecha","lugar","descripcion")

class EquiposAdmin(admin.ModelAdmin):
    list_display=("idEquipo","deporte","campeonato","nombre_eq","num_integrantes")

class DesafiosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Desafios._meta.fields]

class RendimientoAdmin(admin.ModelAdmin):
    llist_display = [field.name for field in Rendimiento._meta.fields]



admin.site.register(Usuario,UsuariosAdmin)
admin.site.register(Deporte,DeporteAdmin)
admin.site.register(Campeonato,CampeonatoAdmin)
admin.site.register(Eventos,EventosAdmin)
admin.site.register(Equipos,EquiposAdmin)
admin.site.register(Desafios,DesafiosAdmin)
admin.site.register(Rendimiento,RendimientoAdmin)

