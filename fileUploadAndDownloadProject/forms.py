from django.forms import ModelForm
from django import forms
from .models import Files


class UploadForm(ModelForm):
    name = forms.TextInput()
    document = forms.FileField()

    class Meta:
        model = Files
        fields = ['name', 'document']
