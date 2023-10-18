from django import forms
from .models import Problem


class ProblemSubmissionForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['name', 'telephone', 'email', 'description', 'priority']
