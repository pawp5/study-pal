from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

        
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32)
    matric_no = forms.CharField(max_length=32)
    dept = forms.CharField(max_length=64)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'matric_no', 'dept', 'password1', 'password2']
        labels = {'first_name' : '', 'last_name': '', 'username': 'Username', 'password1': '', 'password2': '', 'matric_no': '', 'dept': ''}
        widgets  = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'dept': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'matric_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matric Number'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
            }