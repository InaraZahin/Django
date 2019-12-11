from django import forms

from .models import ContactU


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactU
        fields = ('name', 'email', 'phone', 'subject', 'message', )