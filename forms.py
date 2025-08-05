from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email']
        labels = {
            "name": "Devesh Patil",
            "email": "patildevesh6707@gmail.com",
        }

        def clean_name(self):
            name = self.cleandata.get('name')
            if len(name) < 2:
                raise forms.ValidationError("Name Must be atleast 2 characters long.")
            return name
        
        def clean_email(self):
            email = self.cleandata.get('email')
            if not email or '@' not in email:
                raise ValidationError('Enter a valid Email address.')
            return email

