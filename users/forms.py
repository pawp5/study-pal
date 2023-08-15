from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .utils.choices import DEPT_CHOICES, LEVEL_CHOICES

        
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=32)
    matric_no = forms.CharField(max_length=32)
    department = forms.ChoiceField(choices=DEPT_CHOICES)
    school_year = forms.ChoiceField(choices=LEVEL_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'matric_no', 'department', 'school_year', 'password1', 'password2']
        labels = {'username': '', 'first_name' : '', 'password1': '', 'password2': '', 'matric_no': '', 'department': '', 'school_year': ''}
        widgets  = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'deparment': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Department'}),
            'school_year': forms.Select(attrs={'class': 'form-select', 'placeholder': 'School Year'}),
            'matric_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matric Number'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
            }