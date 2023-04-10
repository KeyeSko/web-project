from django.contrib.auth.forms import UserCreationForm

from anecdotator.main.models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
