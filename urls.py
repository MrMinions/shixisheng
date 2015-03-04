from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shixisheng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'shixisheng.views.home'),
    url(r'^lc.html$', 'shixisheng.views.lc'),
    url(r'^fd.html$', 'shixisheng.views.fd'),
    url(r'^time$','shixisheng.views.time'),
    url(r'^upload$','shixisheng.views.upload'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
 	{'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'^admin/', include(admin.site.urls)),
)
