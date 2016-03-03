from django.contrib import admin
from .models import Repository


class RepositoryAdmin(admin.ModelAdmin):
    list_display = ["__str__", "url", "created", "updated"]

    class Meta:
        model = Repository

admin.site.register(Repository, RepositoryAdmin)
