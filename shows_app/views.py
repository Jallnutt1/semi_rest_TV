from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Show
from datetime import datetime

def index(request):
    context = {
        "Shows":Show.objects.all(),
    }
    return render (request, "index.html", context)


def new(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    elif request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            show = Show.objects.create(title=request.POST['title'],network=request.POST['network'],release=request.POST['release'],desc=request.POST['desc'])
            return redirect(f"/shows/{show.id}")


def edit(request, show_id):
    if request.method == 'GET':
        get_show = Show.objects.get(id=show_id)
        str_date = get_show.release.strftime("%Y-%m-%d")

        context={
            'show':get_show,
            'release_date':str_date
        }
        return render(request,'edit.html',context)

    elif request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/shows/{show_id}/edit")
        else:
            show = Show.objects.get(id=request.POST['ID'])
            str_date = show.release.strftime("%Y-%m-%d")

            if request.POST['title'] != show.title:
                show.title = request.POST['title']
            if request.POST['network'] != show.network:
                show.network = request.POST['network']
            if request.POST['release'] != str_date:
                show.release = request.POST['release']
            if request.POST['desc'] != show.desc:
                show.desc = request.POST['desc']
            show.save()
            return redirect('/shows')



def feature(request, show_id):
    if request.method == 'GET':
        context={
            'show':Show.objects.get(id=show_id)
        }
        return render(request,'feature.html',context)


def delete(request,show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/shows')

