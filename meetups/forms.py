from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='pls enter ur email')