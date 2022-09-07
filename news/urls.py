from django.urls import path
from news.views import NewsListView
from news.views import NewsDetailView

urlpatterns = [
  path('', NewsListView, name='news_list'),
  path('<int:pk>/', NewsDetailView, name='news_detail'),
]
