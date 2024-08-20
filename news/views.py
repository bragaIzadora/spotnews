from django.shortcuts import render, get_object_or_404
from news.models import News


def index(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {"news_list": news_list})


def news_details(request, id):
    news = get_object_or_404(News, pk=id)
    return render(request, 'news_details.html', {'news': news})
