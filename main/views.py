from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context: dict = {
        'title': 'OnlineShop - Главная страница',
        'content': "OnlineShop: Онлайн-магазин для всех ваших потребностей"
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict = {
        'title': 'OnlineShop - О нас',
        'content': "Обо мне",
        'text_on_page': "Привет! Меня зовут Варяниця Илья, и я создатель этого проекта."
                        " В этом проекте я стараюсь применить все знания и навыки, "
                        "которые я приобрел, и создать максимально полезный и удобный магазин."
                        "Спасибо, что посетили мой проект по созданию интернет-магазина!"
    }

    return render(request, 'main/about.html', context)