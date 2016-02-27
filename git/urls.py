from django.conf.urls import url

from git import views

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),
    # /repository/add/
    url(r'^repository/add$', views.add, name='add repository'),
]
