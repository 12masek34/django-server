from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Blog


def index(request):
    user = User.objects.get(pk=2)
    blogs = Blog.objects.first()
    # print(user.blog_set.all())
    context = {}
    return render(request, 'app/index.html', context)
