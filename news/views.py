from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import ListView
from news.models import News

def NewsListView(request):

    ones = News.objects.all()
    context = {
      'ones' : ones
    }
    return render(request, 'news/news_list.html', context)

def NewsDetailView(request,pk):

    one = News.objects.get(id=pk)
    context = {
        'one' : one
    }
    return render(request, 'news/news_detail.html', context)
