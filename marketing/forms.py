from .models import Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=('name','email','phone','address','msg',)

