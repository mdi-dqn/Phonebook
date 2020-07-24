from django import forms
from .models import Contact, Phone

class contactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['typeContact', 'fullName', 'image', 'address', 'description']
        widgets = {
            'description' : forms.Textarea,
        }

class phoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['typePhone', 'number']
        widgets = {
            'number': forms.NumberInput()
        }
