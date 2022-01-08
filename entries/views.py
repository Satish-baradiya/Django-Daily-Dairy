from django.shortcuts import render
from . models import Entry

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
        title = request.POST['title']
        content = request.POST['content']
        date_created = request.POST['date']

    return render(request,'entries/newentry.html')

