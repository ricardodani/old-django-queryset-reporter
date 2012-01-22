# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models

_NULL = {'null': True, 'blank': True}
_CHAR = {'max_length':255}
_CNULL = _CHAR
_CNULL.update(_NULL)

class Periodo(models.Model):

    # início do período em que pode ser baixado os relatórios
    inicio = models.DateTimeField(_('início'))
    
    # termino do periodo em que pode ser baixado os relatórios
    termino = models.DateTimeField(_('término'))
    
    # gera um uuid automaticamente para dara acesso ao arquivo de relatório
    senha = models.CharField(_('senha'), editable=False, **_CHAR)
    
    # define se o relatório envia email's
    enviar_email = models.BooleanField(
        _('enviar e-mail`s'), default=False, **_NULL
    )

    # define se o relatório está ativo
    ativo = models.BooleanField(_('ativo'), default=True, **_NULL)

    emails_extra = models.TextField(
        _('e-mail`s extras'), help_text=_('separados por vírgulas'), **_CNULL
    )

    def __unicode__(self):
        return u'%s - %s' % (self.inicio, self.termino)

    class Meta:
        verbose_name = _('período debugável')
        verbose_name_plural = _('períodos debugáveis')

class Arquivo(models.Model):

    periodo = models.ForeignKey(
        Periodo, verbose_name=_('período'), editable=False
    )

    arquivo = models.FileField(editable=False)

    gerado_em = models.DateTimeField(
        _('gerado em'), auto_now_add=True, editable=False
    )
    
    gerado_por = models.ForeignKey(
        User, verbose_name=_('gerado por'), editable=False, **_NULL
    )
    
    enviado_por_email = BooleanField(_('enviado por e-mail'), editable=False)

    class Meta:
        verbose_name = _('arquivo de relatório')
        verbose_name_plural = _('arquivos de relatório')

