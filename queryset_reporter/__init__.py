# -*- encoding: utf-8 -*-

from datetime import datetime

from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from queryset_reporter.models import Periodo

class QuerysetReporter(object):
    '''QuerysetReporter object'''

    def __init__(self, queryset, request, *args, **kwargs):

        self.queryset = queryset
        self.request = request
        
        if self._requisicao_valida(request):
            messages.info(request, _(u'requisição de relatório válida'))
    
    def _requisicao_valida(self, request):
        '''Método interno que verifica se a requisição é valida buscando
        por um período debugável na base.
        '''

        if request.method == 'GET':
            senha = request.GET.get('senha', None)
            now = datetime.now()
            if senha:
                try:
                    self.periodo = Periodo.objects.get(
                        senha=senha, inicio__lte=now, termino__gte=now,
                        ativo=True
                    )
                    return True
                except Periodo.DoesNotExist:
                    pass
            
        return False

    def get_queryset(self):
        '''Retorna a queryset'''
        return self.queryset
