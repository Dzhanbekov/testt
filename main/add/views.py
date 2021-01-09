from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView, UpdateView



def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'add/news_home.html', {'news': news})


class NewsDetail(DetailView):
    model = Articles
    template_name = 'add/details_view.html'
    context_object_name = 'article'


