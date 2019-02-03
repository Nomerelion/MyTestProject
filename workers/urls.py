from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'workers'
urlpatterns = [
    url(r'tree/$', views.show_tree, name='tree'),
    url(r'', views.index, name='index')
]