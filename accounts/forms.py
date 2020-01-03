from django import forms


class UserForm(forms.Form):
    username = forms.SlugField()
    password = forms.CharField(widget=forms.PasswordInput)
