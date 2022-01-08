from django.shortcuts import render
from . models import Entry
from django.http import HttpResponse

# Create your views here.


def index(request):
    entries = Entry.objects.all().order_by("-date_created")
    context = {'entries': entries}
    return render(request, 'entries/entry.html', context)


def content(request, pk_test):
    entry = Entry.objects.get(id=pk_test)
    context = {'entry': entry}
    return render(request, 'entries/content.html', context)


def entry(request):
    if request.method == "POST":
        entry = Entry()
        title = request.POST['title']
        content = request.POST['content']
        date_created = request.POST['date']
        if title and content and date_created:
            entry.title = title
            entry.content = content
            entry.date_created = date_created
            entry.save()
            message = "Added succesfully"
            return render(request, 'entries/entry.html', {
                "entries": Entry.objects.all().order_by("-date_created")
            })
        else:
            return render(request,'entries/newentry.html',{
                "message":"All fields are required"
            })

    return render(request, 'entries/newentry.html')
