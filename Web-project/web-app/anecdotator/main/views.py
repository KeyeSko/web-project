import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View, generic

from .forms import UserCreationForm, AnecdotModelForm
from .models import Anecdot, Like


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def family(request):
    qs = Anecdot.objects.all()

    # initials
    p_form = AnecdotModelForm()
    post_added = False

    profile = request.user
    # profile = User.objects.get(user=request.user)

    if 'submit_p_form' in request.POST:
        print(request.POST)
        p_form = AnecdotModelForm(request.POST, request.FILES)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = AnecdotModelForm()
            post_added = True

    context = {
        'qs': qs,
        'profile': profile,
        'p_form': p_form,
        'post_added': post_added,
    }

    return render(request, 'main/family.html', context)


def contacts(request):
    return render(request, 'main/contacts.html')


@login_required
def profile(request):
    return render(request, 'main/profile.html')


class AnecListView(generic.ListView):
    model = Anecdot

    context_object_name = 'anec_list'

    template_name = 'main/family.html'



def anecdot_list_view(request):
    qs = Anecdot.objects.all()

    # initials
    p_form = AnecdotModelForm()
    post_added = False

    profile = request.user
    # profile = User.objects.get(user=request.user)

    if 'submit_p_form' in request.POST:
        print(request.POST)
        p_form = AnecdotModelForm(request.POST, request.FILES)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = AnecdotModelForm()
            post_added = True

    context = {
        'qs': qs,
        'profile': profile,
        'p_form': p_form,
        'post_added': post_added,
    }

    return render(request, 'main/test.html', context)


@login_required
def like_unlike_post(request):
    print(request.GET)
    if request.method == 'GET':
        anec_id = request.GET.get('anec_id')
        print(anec_id)
        anec_obj = Anecdot.objects.get(id=anec_id)
        profile = request.user
        if profile in anec_obj.liked.all():
            anec_obj.liked.remove(profile)
        else:
            anec_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, anecdot_id=anec_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'

            anec_obj.save()
            like.save()

        data = {
            'value': like.value,
            'likes': anec_obj.liked.all().count()
        }

        return JsonResponse(data, safe=False)

    print(request.POST)
    if request.method == 'POST':
        post_id = request.POST.get('anec_id')
        print(post_id)
        post_obj = Anecdot.objects.get(id=post_id)
        profile = request.user
        # profile = User.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, anecdot_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'

            post_obj.save()
            like.save()

        data = {
            'value': like.value,
            'likes': post_obj.liked.all().count()
        }
        print('lfsdifa')
        print(data)

        return HttpResponse(json.dumps(data), content_type="application/json")
    return redirect('main-post-view')


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
