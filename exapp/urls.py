from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'exapp.views',
    url(r'^$', 'index', name='index'),
    url(r'^reimburse/$', 'reimburse', name='reimburse'),
    url(r'^create/$', 'create', name='create'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^accounts/login/$', 'aclogin', name='aclogin'),
    url(r'^accounts/logout/$', 'aclogout', name='aclogout'),      
 )
