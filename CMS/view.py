from django.shortcuts import render
from .models import *

def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'column.html', {'column': column})


