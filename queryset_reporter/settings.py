# -*- encoding: utf-8 -*-

from django.conf import settings

# defina aqui um local apropriado para os arquivos serem baixados
try:
    REPORTER_FILES = settings.REPORTER_FILES
except:
    REPORTER_FILES = '/tmp/'
