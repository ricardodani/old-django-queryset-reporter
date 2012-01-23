# -*- encoding: utf-8 -*-

from django.conf import settings

# defina aqui um local apropriado para os arquivos serem baixados
REPORTER_FILES = getattr(settings, 'REPORTER_FILES', '/home/ricardo/relatorios/')
