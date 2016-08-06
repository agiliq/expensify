from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('exapp.urls')),
    url('google/', include('social.apps.django_app.urls', namespace='social')),
    url('google/login/google-oauth2/', 'social.apps.django_app.views.auth', name='login')
    
)

urlpatterns += staticfiles_urlpatterns()
