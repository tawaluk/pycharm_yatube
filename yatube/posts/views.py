from django.shortcuts import render
from .models import Post

def index(request):
    template = 'posts/index.html'

    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template_2 = 'posts/group_list.html'
    title_2 = 'Здесь будет информация о группах проекта Yatube'
    var_title_2 = {
        'title_2': title_2,
    }
    return render(request, template_2, var_title_2)
