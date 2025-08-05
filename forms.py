from django import forms
from django.core.validators import validate_email
from django.core exceptions import ValidatitionError
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email']
        labels = {
            "name": "Your Full name",
            "email": "Your Email address",
        }

        def clean_name(self):
            name = self.cleaned_data.get('name')
            if len(name) < 2:
                raise forms.ValidationError("Name Must be atleast 2 characters long.")
            return name
        
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if not email or '@' not in email:
                raise forms.ValidationError('Enter a valid Email address.')
            return email

