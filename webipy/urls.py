from django.conf.urls import patterns, include, url
from django.contrib import admin

from main.views import master_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<fname>\w+)', master_view),
)
