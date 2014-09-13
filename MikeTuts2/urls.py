from django.conf.urls import patterns, include, url
# from article.views import HelloTemplate

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^hello/$', 'article.views.hello'),
    # url(r'^hello_template/$', 'article.views.hello_template'),
    # url(r'^hello_template_simple/$', 'article.views.hello_template_simple'),
    # url(r'^hello_class_view/$', HelloTemplate.as_view()),
    (r'^articles/', include('article.urls')),
    # url(r'^$', 'MikeTuts2.views.home', name='home'),
    # url(r'^MikeTuts2/', include('MikeTuts2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
