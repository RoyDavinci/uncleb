from django import forms

from .models import Work


class AddWork(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
