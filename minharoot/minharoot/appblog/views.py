from django.shortcuts import render

# Create your views here.
from django.http import request
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'appblog/post_list.html', {'posts': posts})
