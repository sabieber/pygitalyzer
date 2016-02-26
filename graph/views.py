from django.shortcuts import render


def index(request):
    return render(request, "graph/index.html", {})


def detail(request, graph_type):
    return render(request, "graph/detail.html", {})
