from django import forms

from .models import Text, TimeTable


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a message'})
            }
        
class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ['mon', 'tue', 'wed', 'thu', 'fri']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a message'})
            }