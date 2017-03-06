from django import forms
from .models import FileUpload



class UploadForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))

    class Meta:
        model = FileUpload
        fields = ['files']
