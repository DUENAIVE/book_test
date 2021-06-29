from django.urls import path
from .views import *



urlpatterns = [

    path('author', AuthorView.as_view(), name=''),
    path('book', BookView.as_view(), name=''),

]