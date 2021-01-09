from django.shortcuts import render


def index(request):
    return render(request, 'news/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'news/about.html')

def contacts(request):
    return render(request, 'news/contact.html')