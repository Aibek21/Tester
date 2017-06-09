from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^parse/', views.parse, name='parse'),
    url(r'^clear/', views.clear, name='clear'),
    url(r'^result/', views.test_result, name='result'),
    url(r'^variant/(?P<pk>\d+)/$', views.variant_detail, name='variant_detail'),
    url(r'^course/(?P<pk>\d+)/$', views.variant_list, name='variant_list'),


    # url(r'^api/getAllVariants/$', views.variant_list),
    # url(r'^api/getTasksByVariant/(?P<pk>\d+)/$', views.variant_tasks_list),
]
