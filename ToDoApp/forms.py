from django import forms
from .models import *

class ToDoForm(forms.Form):
    text = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Add Todo'}
    ))

class newTodo(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = [
            'text',
        ]