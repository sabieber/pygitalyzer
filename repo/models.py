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

    def init_repo(self):
        if hasattr(self, 'repo'):
            self.repo = Repo.init(self.get_local_repo_dir())
            self.origin = self.repo.create_remote('origin', self.url)

    def checkout(self):
        self.init_repo()
        print("Initializing repository")
        self.origin.fetch()
        print("Pulling from remote url")
        self.origin.pull(self.origin.refs[0].remote_head)
        print("Done")
