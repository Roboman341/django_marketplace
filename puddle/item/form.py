from django import forms
from .models import Item

input_classes = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            "category",
            "name",
            "description",
            "price",
            "image",
        )

        widgets = {  # a different way of styling
            "category": forms.Select(attrs={"class": input_classes}),
            "name": forms.TextInput(attrs={"class": input_classes}),
            "description": forms.Textarea(attrs={"class": input_classes}),
            "price": forms.TextInput(attrs={"class": input_classes}),
            "image": forms.FileInput(attrs={"class": input_classes}),
        }
