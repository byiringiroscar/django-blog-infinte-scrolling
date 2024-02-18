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
