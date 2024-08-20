from django.shortcuts import render, get_object_or_404, redirect
from news.models import News
from .forms import CategoryForm


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


# def news_form(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             news = form.save()
#             return redirect('home-page')
#     else:
#         form = NewsForm()
#     context = {
#         'form': form,
#         'authors': User.objects.all(),
#         'categories': Category.objects.all()
#     }

#     return render(request, 'news_form.html', context)
