from django import forms
from django.core import validators

class Student(forms.Form):
    def starts_with_s(value):
        if value[0] != "S":
            raise forms.ValidationError('Name must begin with S')
        
    name = forms.CharField(validators =[starts_with_s])
    email = forms.EmailField()
    age = forms.IntegerField()
    
    
