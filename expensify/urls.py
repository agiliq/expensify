from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^logout/$', 'exapp.views.logout', name='auth_logout'),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('exapp.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'exapp.views.index', name='index'), 
)

urlpatterns += staticfiles_urlpatterns()
