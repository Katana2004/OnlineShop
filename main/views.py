from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context: dict = {
        'title': 'Home',
        'content': 'Welcome to Online Shop!',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_autenticated': False
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse("Hello, world.")