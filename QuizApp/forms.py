from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	userName = forms.CharField(label='User', max_length =100)
	passWord = forms.CharField(label="Password", max_length=100, widget =forms.PasswordInput())
