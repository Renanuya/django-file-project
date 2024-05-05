from django.forms import ModelForm
from django import forms
from .models import Files


# This class is used to create a form for file upload.
# It inherits from Django's ModelForm.
# It has two fields: 'name' and 'document'.
# 'name' is a TextInput and 'document' is a FileField.
class UploadForm(ModelForm):
    name = forms.TextInput()
    document = forms.FileField()

    # Meta class is used to provide additional information about the form.
    # Here, it specifies the model to use and the fields to include in the form.
    class Meta:
        model = Files
        fields = ['name', 'document']


# This class is used to create a form for renaming a file.
# It inherits from Django's Form.
# It has one field: 'new_name'.
# 'new_name' is a CharField with a label 'New Name' and a maximum length of 100 characters.
class RenameFileForm(forms.Form):
    new_name = forms.CharField(label='New Name', max_length=100)
