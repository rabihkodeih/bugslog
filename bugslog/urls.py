from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from main.views import testpage
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'idlts_website.views.home', name='home'),
    # url(r'^idlts_website/', include('idlts_website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # app:
    #url(r'^bugslog/testview/', views.testview),
    
    # API ajax:
    #url(r'^bugslog/testajax/', views.testajax),

    # admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(admin.site.urls)),
    
    url(r'^index/', testpage)
    
)
