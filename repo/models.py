from __future__ import absolute_import
from os.path import join

from django.db import models
from git import Repo
from pygitalyzer.settings import BASE_DIR


class Repository(models.Model):
    url = models.URLField(verbose_name="Repository Clone URL", unique=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    def checkout(self):
        repo = Repo.clone_from(self.url, join(BASE_DIR, 'repo', self.id))
        print(repo.bare)
