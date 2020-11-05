from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = "username"
        self.fields['username'].help_text = "alphanumerics and @/./+/-/_ only"

        self.fields['email'].label = "email"

        self.fields['password1'].label = "password"
        self.fields['password1'].help_text = "at least 8 characters. can’t be entirely numeric"

        self.fields['password2'].label = "confirm password"
        self.fields['password2'].help_text = ""
