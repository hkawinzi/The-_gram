from django import forms

class LoginForms(forms.Form):
    your-name = forms.CharField(label= 'Your name,Username or Email', max_length=300)
    your-password = forms.CharField(label='your password', max_length=20)