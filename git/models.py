from django.db import models


class Repository(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=120, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()

    def __str__(self):
        return self.name
