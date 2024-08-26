from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from news.models import News, User, Category
from .forms import CategoryForm, NewsForm
from .serializers import CategorySerializer, UserSerializer


def index(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {"news_list": news_list})


def news_details(request, id):
    news = get_object_or_404(News, pk=id)
    return render(request, 'news_details.html', {'news': news})


def category_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = CategoryForm()

    return render(request, 'categories_form.html', {'form': form})


def news_form(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = NewsForm()

    users = User.objects.all()
    categories = Category.objects.all()
    return render(request, 'news_form.html',
                  {'form': form, 'users': users, 'categories': categories})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
