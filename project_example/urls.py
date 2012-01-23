from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_example.views.home', name='home'),
    # url(r'^project_example/', include('project_example.foo.urls')),
    url(r'^$', 'project_example.views.post_list'),
    (r'^', include('basic.blog.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
