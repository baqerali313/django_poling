from django import forms
from .models import Images


class FormImage(forms.ModelForm):
    class Meta:
        model = Images
        fields = '__all__'
        labels = {'image': ''}
