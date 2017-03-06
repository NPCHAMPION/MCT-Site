from django.shortcuts import render
from django.template import Context

# Create your views here.

def index(request):
    context = Context({
        'title': 'Home',
        'header': 'Home Page!',
        'home-nav-active': 'active',
        })
    return render(request, 'home_index.html', context)

def contact(request):
    return render(request, '')