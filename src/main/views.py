from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def list_from_api(request):
    return render(request, 'main/list.html')
