from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^parse/', views.parse, name='parse'),
    url(r'^clear/', views.clear, name='clear'),
    url(r'^variant/(?P<pk>\d+)/$', views.variant_detail, name='variant_detail'),

]
