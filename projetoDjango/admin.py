from django.contrib import admin

# Register your models here.
from .models import Zona, Localidade, Bairro, Municipio, ModalidadeTransporte


class ZonaAdmin(admin.ModelAdmin):
    model = Zona()
    list_display = ('id', 'descricao')
    list_per_page = 10


class LocalidadeAdmin(admin.ModelAdmin):
    model = Localidade
    list_display = ('id', 'descricao', 'id_zona')
    list_per_page = 10


class BairroAdmin(admin.ModelAdmin):
    model = Bairro
    list_display = ('id', 'descricao')
    list_per_page = 10


class MunicipioAdmin(admin.ModelAdmin):
    model = Municipio
    list_display = ('id', 'descricao', 'uf')
    list_per_page = 10


class ModalidadeTransporteAdmin(admin.ModelAdmin):
    model = ModalidadeTransporte
    list_display = ('id', 'descricao')
    list_per_page = 10


admin.site.register(Zona, ZonaAdmin)
admin.site.register(Localidade, LocalidadeAdmin)
admin.site.register(Bairro, BairroAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(ModalidadeTransporte, ModalidadeTransporteAdmin)
