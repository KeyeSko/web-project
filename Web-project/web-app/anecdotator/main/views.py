from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserCreationForm


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


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
