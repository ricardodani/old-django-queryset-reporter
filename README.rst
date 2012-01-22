==================================
django-queryset-reporter - Uma ferramenta djangônica para relatório de queries
==================================

A idéia principal
================

* Na view onde a queryset é enviada para o ``QuerysetReporter`` .
* O ``QuerysetReporter`` pega os valores da queryset usando ``.values()`` ou ``.values_list()``
* O valueslist então vai possuir poder de todo o resultado em uma estrutura de dados, com todas as colunas que são interessantes.
* Com isso ele vai gerar um resultado, exibindo também, talvez o sql gerado, o link do arquivo sem senha, quem gerou, o horario usando o Rogerio Reports, ou um gerador de .xls , .pdf, open office calc, etc.
* Esse resultado será disponibilizado no sistema, e também enviado por e-mail para um dos destinatarios.

Armazenamento do relatório.
===============

* Para armazenar o relatório e ter controle sobre como ele deve ser executado, um modelo será construido e adicionado ao modulo django.admin.

	Modelo:

		Período debugável:

			Campos: id, inicia em, termina em, password (ou uuid), lista de arquivos, enviar_emails, emails_extras

		Arquivos de relatório:

			Campos: id, periodo_id, gerado_em, gerado_por, enviado_por_email,

Execução do relatório
==============

* Atravéz de uma url GET com a senha do periodo debugável

Observações importantes
==============

* Instalação:

    - O ``basic.blog`` ao ser instalado no seu ambiente, não copia a pasta `templates` para a lib. Sendo assim, fiz um link simbólico na mão para esta pasta.
