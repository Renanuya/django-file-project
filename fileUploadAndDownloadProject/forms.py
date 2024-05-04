from django.forms import ModelForm
from django import forms
from .models import Files


class UploadForm(ModelForm):
    name = forms.TextInput()
    document = forms.FileField()

    class Meta:
        model = Files
        fields = ['name', 'document']


class RenameFileForm(forms.Form):
    new_name = forms.CharField(label='New Name', max_length=100)
