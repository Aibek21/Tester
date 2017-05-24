from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^parse/', views.parse, name='parse'),
    url(r'^parse2/', views.parse2, name='parse2'),
    url(r'^parse3/', views.parse3, name='parse3'),
    url(r'^parse4/', views.parse4, name='parse4'),
    url(r'^parse5/', views.parse5, name='parse5'),
    url(r'^clear/', views.clear, name='clear'),
    url(r'^result/', views.test_result, name='result'),
    url(r'^variant/(?P<pk>\d+)/$', views.variant_detail, name='variant_detail'),


    # url(r'^api/getAllVariants/$', views.variant_list),
    # url(r'^api/getTasksByVariant/(?P<pk>\d+)/$', views.variant_tasks_list),
]
