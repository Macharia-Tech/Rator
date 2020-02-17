from django import forms
from .models import Profile,Project,Rating

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['editor','profile','pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }