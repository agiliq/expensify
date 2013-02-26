from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'exapp.views',
    url(r'^$', 'index', name='index'),
    url(r'^all_claims', 'all_claims', name='all_claims'),
    url(r'^reimburse/$', 'reimburse', name='reimburse'),
    url(r'^create/$', 'create', name='create'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^openid/logout/$', 'oidlogout', name='oidlogout'),      
 )
