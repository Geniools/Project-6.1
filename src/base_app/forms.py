from django import forms
from django.core.validators import FileExtensionValidator


# This was meant as a workaround for the multiple file upload issue, but it does not work. (taken from official Django docs)
# https://docs.djangoproject.com/en/4.2/topics/http/file-uploads/#uploading-multiple-files
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)
    
    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


# Due to a recent Django update, multiple files cannot be uploaded at once because of security reasons.
class UploadMT940Form(forms.Form):
    file = MultipleFileField(
        label="Select an MT940 file:", allow_empty_file=False, widget=forms.ClearableFileInput(attrs={"accept": ".sta, .txt", "allow_multiple_selected": True}),
        validators=[FileExtensionValidator(allowed_extensions=["sta", "txt"])]
    )
