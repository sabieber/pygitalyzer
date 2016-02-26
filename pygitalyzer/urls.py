from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

import graph.urls
from pygitalyzer import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^graph/', include(graph.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
