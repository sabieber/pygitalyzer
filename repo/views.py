from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_safe

from repo.models import Repository
from .forms import RepositoryForm


@require_safe
def index(request):
    context = {
        'form': RepositoryForm(),
        'repositories': Repository.objects.all(),
    }
    return render(request, "repo/index.html", context)


@require_POST
def add(request):
    form = RepositoryForm(request.POST)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.full_clean()
        instance.save()

    return redirect("repo:repositories")


@require_safe
def remove(request, id=None):
    repository = get_object_or_404(Repository, id=id)
    repository.delete()
    messages.success(request, "Successfully deleted")
    return redirect("repo:repositories")
