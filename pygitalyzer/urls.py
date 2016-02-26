from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

import graph.urls
import git.views

urlpatterns = [
    url(r'^$', git.views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^graph/', include(graph.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
