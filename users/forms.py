from django import forms
from django.contrib.auth.models import User

from .models import ProfileModel


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['photo', 'date_of_birth', 'address']



    
