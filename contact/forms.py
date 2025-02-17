from django import forms
from .models import contactUsModel

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = contactUsModel
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your Email'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Your Message'})