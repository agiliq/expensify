from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'exapp.views',
    url(r'^$', 'index', name='index'),
    url(r'^all_claims', 'all_claims', name='all_claims'),
    url(r'^approved_claims', 'approved_claims', name='approved_claims'),
    url(r'^reimburse/$', 'reimburse', name='reimburse'),
    url(r'^reimburse/(?P<id>\d+)$', 'reimburse', name='reimburse'),
    url(r'^create/$', 'create', name='create'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^openid/logout/$', 'oidlogout', name='oidlogout'),
)
