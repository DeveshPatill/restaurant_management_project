from django import forms
from .models import Feedback,MenuItem,ContactForm,NewsletterSubscriber


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment']
        widgets = {
            'comment'= forms.Textarea(attrs{'rows':4, 'placeholder': 'Enter your feedback here'})
        }

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name','description','price','image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']
        error_messages = {
            "email" : {
                "invalid":"Please enter a valid email address",
                "required":"Email is required"
            },
            "message" : {
                "required":"message cannot be empty"
            }
        }

class NewsletterSubscriber(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email':forms.EmailInput(attrs={'placeholder':'Enter your email','class':'form-control'})
        }

        