from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Blog


def index(request):
    context = {}
    return render(request, 'app/index.html', context)
