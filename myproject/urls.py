from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^concesionario$', "cms_users_put.views.concesionario"),
    url(r'^concesionario/precio/(.*)$', "cms_users_put.views.info"),
    url(r'^(.*)$', "cms_users_put.views.notFound"),
    
)
