from django.shortcuts import render, HttpResponse
from portafolio.models import Profile

def home(request):

    profile = Profile.objects.first()

    return render(request, 'core/home.html', {
        'profile': profile
    })

def about(request):
    profile = Profile.objects.first()
    return render(request, "core/about.html", {
        'profile': profile
    })

def portfolio(request):
    profile = Profile.objects.first()
    return render(request, "core/../portafolio/templates/portafolio/portafolio.html", {
        'profile': profile
    })

def contact(request):
    profile = Profile.objects.first()
    return render(request, "core/contact.html", {
        'profile': profile
    })