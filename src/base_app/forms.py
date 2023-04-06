from django import forms
from django.core.validators import FileExtensionValidator


class UploadMT940Form(forms.Form):
	file = forms.FileField(
		label="Select an MT940 file:", allow_empty_file=False, widget=forms.ClearableFileInput(attrs={"accept": ".sta, .txt", "multiple": True}),
		validators=[FileExtensionValidator(allowed_extensions=["sta", "txt"])]
	)
