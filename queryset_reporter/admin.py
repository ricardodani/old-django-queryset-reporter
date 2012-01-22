# -*- encoding: utf-8 -*-

from django.contrib import admin
from queryset_reporter.models import Periodo, Arquivo


class PeriodoAdmin(admin.ModelAdmin):
    list_display  = ('__unicode__', 'inicio', 'termino', 'senha', 'enviar_email', 'ativo')
    list_filter = ('inicio', 'termino', 'enviar_email', 'ativo')
    search_field = ('emails_extra',)
admin.site.register(Periodo, PeriodoAdmin)

class ArquivoAdmin(admin.ModelAdmin):
    list_display  = (
        'arquivo', 'periodo', 'gerado_em', 'gerado_por', 'enviado_por_email'
    )
    list_filter = ('gerado_em',)
admin.site.register(Arquivo, ArquivoAdmin)

