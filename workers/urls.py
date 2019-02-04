from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'workers'
urlpatterns = [
    url(r'workers_table/$', views.show_data, name = 'Workers Table'),
    url(r'table/$', views.table, name = 'table'),
    url(r'tree/$', views.show_tree, name='tree'),
    url(r'', views.index, name ='index'),
]