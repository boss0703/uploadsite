from django import forms

from upload.models import ImageFileModel


class UploadForm(forms.ModelForm):
    class Meta:
        model = ImageFileModel
        fields = ('image', )
