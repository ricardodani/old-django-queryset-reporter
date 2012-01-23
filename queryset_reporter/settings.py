# -*- encoding: utf-8 -*-

from django.conf import settings

# defina aqui um local apropriado para os arquivos serem baixados
# relativo ao STATIC_ROOT
REPORTER_FILES = getattr(settings, 'REPORTER_FILES', 'relatorios/')
