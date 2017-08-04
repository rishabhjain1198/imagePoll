from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(paren)/$', views.parens, name='parens'),
        url(r'^([0-9]+)/$', views.detail, name='detail'), 
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
        url(r'^(?P<question_id>[0-9]+)/result/$', views.result, name='result'),
        ]
