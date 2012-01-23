# -*- encoding: utf-8 -*-

import uuid
from datetime import datetime

from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from queryset_reporter.models import Periodo, Arquivo
from queryset_reporter.settings import REPORTER_FILES

# TODO: primeira coisa a fazer, gerar HTML mesmo,
# substituir a saida no get_queryset()
#
# também abrir opção na API para setar a queryset um momento
# depois de inicializar o objeto. Ou simplesemnte criar um parametro callback
# que se setado, usa a queryset em questão caso falhe a token.
    
class QuerysetReporter(object):
    '''QuerysetReporter object'''

    def __init__(self, queryset, request, *args, **kwargs):

        self.queryset = queryset
        self.request = request
        
        if self._requisicao_valida(request):
            self.values = self.queryset.values()
            self._cria_arquivo()
            messages.error(request, _(u'arquivo criado: %s' % self.path))

    def _requisicao_valida(self, request):
        '''Método interno que verifica se a requisição é valida buscando
        por um período debugável na base.
        '''

        if request.method == 'GET':
            self.token = request.GET.get('token', None)
            self.now = datetime.now()
            if self.token:
                try:
                    self.periodo = Periodo.objects.get(
                        token=self.token, inicio__lte=self.now,
                        termino__gte=self.now, ativo=True
                    )
                    return True
                except Periodo.DoesNotExist:
                    pass
            
        return False

    def _renderiza_html(self):
        template = 'reporter.html'
        context = {
            'title': self.filename,
            'thead': [
                key for key in self.values[0]
            ] if self.values else None,
            'tbody': self.values,
        }
        return render_to_string(template, context)

    def _salva_arquivo(self):
        self.arquivo = Arquivo(
            periodo=self.periodo, arquivo=self.path,
            gerado_por=self.request.user
        )
        self.arquivo.save()

    def _cria_arquivo(self):
        self.filename = "%s_%s.html" % (self.token, str(uuid.uuid4())[:8])
        path = "%s%s" % (REPORTER_FILES, self.filename)

        self.path = default_storage.save(
            path, ContentFile(self._renderiza_html().encode('utf-8'))
        )

        self._salva_arquivo()

    def get_queryset(self):
        '''Retorna a queryset'''
        return self.queryset
