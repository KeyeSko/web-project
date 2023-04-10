from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView



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


class RegisterUser(CreateView):
    model = User
    template_name = 'registration/register.html'
    success_url = reverse_lazy('profile')
    fields = '__all__'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
