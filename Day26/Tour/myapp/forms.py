from django import forms
from .models import Tour

class Tour_Form(forms.ModelForm):
    class Meta:
        model = Tour
        fields ="__all__"