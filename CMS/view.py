from django.shortcuts import render
from .models import *

def index(request):
    res = {
        'name' : 'xiaoyongjian',
        'addr' : '肇庆鼎湖'
    }
    user(name=res['name'],
         addr=res['addr']).save()
    return render(request, 'base.html', res)