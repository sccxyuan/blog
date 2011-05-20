from django.conf.urls.defaults import *
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from mysite import views
from django.conf import settings


urlpatterns = patterns('mysite.views',
    (r'^$','zhuye'),
    (r'^action/','action'),
    (r'^blog.html','zhu'),
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    (r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^images/(?P<path>.*)$','django.views.static.serve',{'document_root':'/Users/yuanjingyun/mysite/templates/images'}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/yuanjingyun/mysite/templates/css'}),
    (r'^(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__), 'templates')}),
    )