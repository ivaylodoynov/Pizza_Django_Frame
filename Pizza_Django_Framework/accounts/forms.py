from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from Pizza_Django_Framework.accounts.models import Profile

UserModel = get_user_model()


class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields =("email",)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("profile_image",)