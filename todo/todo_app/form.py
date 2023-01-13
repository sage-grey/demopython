from .models import Task
from django import forms
from django.forms.widgets import NumberInput

class ToDoForms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']

        widget={
            'name': forms.TextInput(attrs={'class':"form-control"}),
            'priority': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateField(widget = NumberInput(attrs={'type':'date','class': 'form-control'})),
        }