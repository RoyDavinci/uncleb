from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import AddWork
from django.urls import reverse
from django.core.mail import BadHeaderError, send_mail
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def works(request):
    return render(request, 'our_work.html')


def contact(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        message = request.POST['message']
        if message and email:
            try:
                send_mail('New Message From Personal Website',
                          f"{first_name}-{last_name} \n \n \n {message}", email, ['emsthias33@gmail.com'])
            except:
                return HttpResponse('message error')
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'contact.html')


def create_work(request):
    if request.method == "POST":
        form = AddWork(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AddWork()

    return render(request, 'add-work.html', {'form': form})
