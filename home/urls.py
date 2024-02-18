from django.urls import path
from .views import *


urlpatterns = [
    path('', articles, name='articles'),
]