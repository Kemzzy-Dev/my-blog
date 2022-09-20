from django.forms import ModelForm
from django import forms
from .models import contact
from .models import newsletter


class contactForm(ModelForm):
    class Meta:
        model = contact 
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'subject':forms.TextInput(attrs={'placeholder': 'Your Subject'}),
            'message':forms.Textarea(attrs={'placeholder': 'Your Message'}),
        }


class newsletterForm(ModelForm):
    class Meta: 
        model = newsletter
        fields='__all__'
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'class':'form-control', 'id':'validationCustomUsername'}),
        }