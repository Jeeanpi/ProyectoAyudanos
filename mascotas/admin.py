from django.contrib import admin
from .models import ContratarPlan, Mascota, Cliente

# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "propietario", "raza", "numeroMicroChip"]
    list_editable = ["numeroMicroChip"]
    search_fields = ["nombre", "raza"]
    list_filter = ["raza"]

class ContratarPlanAdmin(admin.ModelAdmin):
    list_display = ["nombreCliente", "nombreMascota", "tipoPlan"]

admin.site.register(Cliente)
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(ContratarPlan, ContratarPlanAdmin)
