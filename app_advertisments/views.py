from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisment
from .forms import AdvertismentForm
from django.urls import reverse


def index(request):
    advertisments = Advertisment.objects.all()
    context = {'advertisments' : advertisments}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render (request, 'top-sellers.html')

def advertisment_post(request):
    if request.method == 'POST':
        form = AdvertismentForm(request.POST, request.FILES)
        if form.is_valid():
            advertisment = Advertisment(**form.cleaned_data)
            advertisment.user = request.user
            advertisment.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertismentForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)