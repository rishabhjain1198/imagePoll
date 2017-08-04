from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.reindex, name='reindex'),
    url(r'^index/$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.questionview, name='questionview'),
]
