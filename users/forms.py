from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your forms here.


class SignUpForm(UserCreationForm, forms.Form):
    bookshelf_name = forms.CharField(max_length=150)
