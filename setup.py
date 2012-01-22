# -*- encoding: utf-8 -*- 

#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-query-reporter',
    version='dev',
    description='a tool to report querysets in pdf to sent a e-mail with the \
report to the site-admins with the values of the fields generated in queryset.\
— Read more',
    author='Ricardo Dani',
    author_email='ricardodani@gmail.com',
    url='https://github.com/ricardodani/django-queryset-reporter',
    packages=['queryset_reporter'],
)
