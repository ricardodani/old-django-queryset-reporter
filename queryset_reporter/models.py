# -*- encoding: utf-8 -*-

import uuid

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings as dj_settings

from queryset_reporter import settings

_NULL = {'null': True, 'blank': True}
_CHAR = {'max_length':255}
_CNULL = _CHAR
_CNULL.update(_NULL)

class Periodo(models.Model):

    # início do período em que pode ser baixado os relatórios
    inicio = models.DateTimeField(_(u'início'))
    
    # termino do periodo em que pode ser baixado os relatórios
    termino = models.DateTimeField(_(u'término'))
    
    # gera um uuid automaticamente para dara acesso ao arquivo de relatório
    token = models.CharField(_(u'token'), editable=False, **_CHAR)
    
    # define se o relatório envia email's
    enviar_email = models.BooleanField(
        _(u'enviar e-mail`s'), default=False
    )

    # define se o relatório está ativo
    ativo = models.BooleanField(_(u'ativo'), default=True)

    emails_extra = models.TextField(
        _(u'e-mail`s extras'), help_text=_(u'separados por vírgulas'), **_CNULL
    )

    def __unicode__(self):
        return u'# %d - %s -> %s' % (self.id, self.inicio, self.termino)

    def save(self, *args, **kwargs):
        self.token = str(uuid.uuid4())[:8]
        super(Periodo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'período debugável')
        verbose_name_plural = _(u'períodos debugáveis')

class Arquivo(models.Model):

    periodo = models.ForeignKey(
        Periodo, verbose_name=_(u'período'), editable=False
    )

    arquivo = models.FileField(
        _(u'arquivo'), editable=False, upload_to=settings.REPORTER_FILES
    )

    gerado_em = models.DateTimeField(
        _(u'gerado em'), auto_now_add=True, editable=False
    )
    
    gerado_por = models.ForeignKey(
        User, verbose_name=_(u'gerado por'), editable=False, **_NULL
    )
    
    enviado_por_email = models.BooleanField(
        _(u'enviado por e-mail'), editable=False
    )

    def __unicode__(self):
        return u"# %s - %s" % (self.periodo.id, self.arquivo)

    def link_arquivo(self):
        return u"<a href=\"%(media_url)s%(arquivo)s\">%(media_url)s%(arquivo)s</a>" % {
            'media_url': dj_settings.MEDIA_URL,
            'arquivo': self.arquivo
        }
    link_arquivo.allow_tags = True
    link_arquivo.short_description = "Link do arquivo"

    class Meta:
        verbose_name = _(u'arquivo de relatório')
        verbose_name_plural = _(u'arquivos de relatório')

