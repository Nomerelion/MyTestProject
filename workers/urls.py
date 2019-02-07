from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views


app_name = 'workers'
urlpatterns = [
    url(r'signup/', views.SignUp.as_view(), name='signup'),
    url(r'home/', TemplateView.as_view(template_name='home.html'), name = 'home'), 
    url(r'workers_table/$', views.show_data, name = 'Workers Table'),
    url(r'table/$', views.table, name = 'table'),
    url(r'show_tree/$', views.show_tree, name = 'show_tree'),
    url(r'tree/$', views.tree, name = 'tree'),
    # url(r'', views.index, name ='index'),
]