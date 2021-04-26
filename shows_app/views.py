from django.shortcuts import render, redirect, HttpResponse
from .models import Show

def index(request):
    context = {
        "Shows":Show.objects.all(),
    }
    return render (request, "index.html", context)

def add_show(request):
    if request.method == 'GET':
        return render(request, 'new_show.html')
    elif request.method == 'POST':
        new_show = Show.objects.create(title=request.POST['title'],network=request.POST['network'],release=request.POST['release'],desc=request.POST['desc'])
        return redirect('/')