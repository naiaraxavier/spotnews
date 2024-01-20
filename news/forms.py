from django import forms
from news.models import Category


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels = {"name": "Nome"}
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "type": "text",
                    "maxlength": "200",
                    "required": "required",
                }
            )
        }
