from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def family(request):
    return render(request, 'main/family.html')


def contacts(request):
    return render(request, 'main/contacts.html')

@login_required
def profile(request):
    return render(request, 'main/profile.html')
