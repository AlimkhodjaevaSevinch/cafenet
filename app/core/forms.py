from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    birthday = forms.DateField(input_formats=("dd:MM:YYYY",))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'phone')


class LogInForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('user', 'email', 'password')