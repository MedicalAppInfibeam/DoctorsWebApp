from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from ProfileApp.models import Profile
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

FIELD_NAME_MAPPING = {
	'username': 'username1',
	'password1': 'password1',
	'password2': 'password2',
	'email': 'email'
}

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = Profile
		fields = ['username', 'password']
		
class UserForm(forms.ModelForm):

	def add_prefix(self, field_name):
        # look up field name; return original if not found
		field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
		return super(UserForm, self).add_prefix(field_name)

	username1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pick a username'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Create a password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your email address'}))

	class Meta:
		model = Profile
		fields = ['username', 'password1', 'password2', 'email']

class PasswordResetEmail(PasswordResetForm):

	class Meta:
		fields = ['email']

