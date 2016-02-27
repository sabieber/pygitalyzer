from django.shortcuts import render
from django.views.decorators.http import require_POST, require_safe

from .forms import RepositoryForm


@require_safe
def index(request):
    context = {
        'form': RepositoryForm(),
    }
    return render(request, "git/index.html", context)


@require_POST
def add(request):
    print(request.POST)
    return render(request, "git/index.html", {})
