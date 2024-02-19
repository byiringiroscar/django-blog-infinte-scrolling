from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Article

# Create your views here.




def articles(request):
    """
    Fetch paginated articles and render them.
    """
    page_number = request.GET.get('page', 1)
    paginator = Paginator(Article.objects.all(), 10)
    page_obj = paginator.get_page(page_number)

    return render(request, 'articles.html', {'page_obj': page_obj})


def search_results_view(request):
    query = request.GET.get('search', '')
    page_number = request.GET.get('page', 1)
    all_articles = Article.objects.all()
    if query:
        articles = all_articles.filter(title__icontains=query)
        paginator = Paginator(articles, 10)
        page_obj = paginator.get_page(page_number)
    else:
        articles = all_articles
        paginator = Paginator(articles, 10)
        page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'count': paginator.count,
    }

    return render(request, 'search_results.html', context)