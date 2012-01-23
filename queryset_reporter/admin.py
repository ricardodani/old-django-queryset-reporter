# -*- encoding: utf-8 -*-

from django.contrib import admin
from queryset_reporter.models import Periodo, Arquivo


class PeriodoAdmin(admin.ModelAdmin):
    list_display  = ('__unicode__', 'inicio', 'termino', 'token', 'enviar_email', 'ativo')
    list_filter = ('inicio', 'termino', 'enviar_email', 'ativo')
    search_field = ('emails_extra',)
admin.site.register(Periodo, PeriodoAdmin)

class ArquivoAdmin(admin.ModelAdmin):
    fields = ('arquivo', 'periodo', 'gerado_em', 'gerado_por', 'enviado_por_email')
    readonly_fields = ('arquivo', 'periodo', 'gerado_em', 'gerado_por', 'enviado_por_email')
    list_display  = (
        '__unicode__', 'link_arquivo', 'periodo', 'gerado_em', 'gerado_por', 'enviado_por_email'
    )
    list_filter = ('gerado_em',)
admin.site.register(Arquivo, ArquivoAdmin)

