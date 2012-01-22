# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

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
    senha = models.CharField(_(u'senha'), editable=False, **_CHAR)
    
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
        return u'%s - %s' % (self.inicio, self.termino)

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

    class Meta:
        verbose_name = _(u'arquivo de relatório')
        verbose_name_plural = _(u'arquivos de relatório')

