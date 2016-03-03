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

    def get_local_repo_dir(self):
        return join(BASE_DIR, 'tmp', 'repo', str(self.id))

    def clone(self):
        print("Creating empty repository")
        repo = Repo.init(self.get_local_repo_dir())
        origin = repo.create_remote('origin', self.url)
        origin.fetch()
        print("Cloning from remote url")
        origin.pull(origin.refs[0].remote_head)
        print("Done")
