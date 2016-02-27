from django import forms

from git.models import Repository


class RepositoryForm(forms.ModelForm):
    class Meta:
        model = Repository
        fields = ['url', 'name']
