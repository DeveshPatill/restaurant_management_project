from django import forms
from utils.validation_utils import is_valid_email

class EmailForm(forms.Form):
    email = forms.CharField()

    def clean_email(self):

        email = self.cleaned_data.get("email")
        if not is_valid_email(email):
            raise forms.validationError("Invalid email format")
        return email