# -*- encoding: utf-8 -*-

from django.conf import settings
from django.views.generic import list_detail

from basic.blog.models import Post
from queryset_reporter import QuerysetReporter

def post_list(request, page=0, paginate_by=20, **kwargs):
    page_size = getattr(settings,'BLOG_PAGESIZE', paginate_by)
    
    qr = QuerysetReporter(Post.objects.published(), request)
    
    return list_detail.object_list(
        request,
        queryset=qr.get_queryset(),
        paginate_by=page_size,
        page=page,
        **kwargs
    )
post_list.__doc__ = list_detail.object_list.__doc__
