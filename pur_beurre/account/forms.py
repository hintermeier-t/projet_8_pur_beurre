from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from .models import User

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password"
        ]
        widget = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),

        }

class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]
        widget = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
        }