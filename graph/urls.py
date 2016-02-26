from django.conf.urls import url

from graph import views

urlpatterns = [
    # /graph/
    url(r'^$', views.index, name='index'),
    # /graph/:graphtype/
    url(r'^(?P<graph_type>[0-9]+)/$', views.detail, name='detail'),
]
