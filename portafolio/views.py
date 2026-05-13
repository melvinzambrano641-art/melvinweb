from django.shortcuts import render
from .models import Portafolio, Profile


def portafolio(request):

    profile = Profile.objects.first()
    projects = Portafolio.objects.all()

    return render(request, 'portafolio/portafolio.html', {
        'projects': projects,
        'profile': profile
    })