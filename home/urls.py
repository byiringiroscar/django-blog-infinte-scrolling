from django.urls import path
from .views import *


urlpatterns = [
    path('', articles, name='articles'),
    path('search/results/', search_results_view, name='search_results_view'),
]