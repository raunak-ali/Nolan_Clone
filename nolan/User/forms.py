from django import forms
from multiselectfield import MultiSelectFormField
from .models import Scripts

class ScriptForm(forms.ModelForm):
    class Meta:
        model = Scripts
        fields = ['title', 'Plot', 'genres']
        widgets = {
            'genres': forms.CheckboxSelectMultiple(),
        }