from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    var_title = {
        'title': title,
    }
    return render(request, template, var_title)


def group_posts(request, slug):
    template_2 = 'posts/group_list.html'
    title_2 = 'Здесь будет информация о группах проекта Yatube'
    var_title_2 = {
        'title_2': title_2,
    }
    return render(request, template_2, var_title_2)
