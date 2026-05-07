from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('book-table', book_table, name='book_table'),

]
