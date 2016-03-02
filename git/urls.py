from django.conf.urls import url

from git import views

urlpatterns = [
    # /
    url(r'^$', views.index, name='repositories'),
    # /repository/add/
    url(r'^repository/add$', views.add, name='add_repository'),
    url(r'^repository/(?P<id>\d+)/remove$', views.remove, name='remove_repository'),
]
