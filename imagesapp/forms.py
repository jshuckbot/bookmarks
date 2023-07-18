from django import forms

from imagesapp.models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["title", "url", "description"]
        widgets = {
            "url": forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data["url"]
        valid_extensions = ["jpg", "jpeg", "png"]
        extensions = url.rsplit(".", 1)[1].lower()
        if extensions not in valid_extensions:
            raise forms.ValidationError("The given URL does not match valid image extensions.")
        return url
