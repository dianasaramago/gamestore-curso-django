from django.contrib import admin

from core.models import Genero, Plataforma, Desenvolvedora, Jogo, Compra, ItensCompra

admin.site.register(Genero)
admin.site.register(Plataforma)
admin.site.register(Desenvolvedora)
admin.site.register(Jogo)

class ItensInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)
