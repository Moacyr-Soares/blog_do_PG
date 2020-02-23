from django.shortcuts import render

# Create your views here.
from django.http import request

def post_list(request):
    return render(request, 'post_list.html', {})
