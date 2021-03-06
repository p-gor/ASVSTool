from django import forms
from django.forms import Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=40, required=True,
                               widget=forms.TextInput(attrs={'class': 'pr', 'title': 'Username'}))
    email = forms.EmailField(max_length=60, required=True,
                             widget=forms.TextInput(attrs={'class': 'pr', 'title': 'Email'}))
    first_name = forms.CharField(max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'class': 'pr', 'title': 'First name'}))
    last_name = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs={'class': 'pr', 'title': 'Last name'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'pr', 'title': 'Password'}))
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'pr', 'title': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'pr', 'title': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'pr', 'title': 'Password'}))


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=40, required=True,
                               widget=forms.TextInput(attrs={'class': 'pr', 'title': 'Username'}))
    email = forms.EmailField(max_length=60, required=True,
                             widget=forms.TextInput(attrs={'class': 'pr', 'title': 'Email'}))
    first_name = forms.CharField(max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'class': 'pr', 'title': 'First name'}))
    last_name = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs={'class': 'pr', 'title': 'Last name'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        widgets = {
            'Image': Textarea(attrs={'class': 'im'}),
        }
