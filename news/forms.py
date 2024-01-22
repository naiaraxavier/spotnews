from django import forms
from news.models import Category, News


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


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        labels = {
            "title": "Título",
            "content": "Conteúdo",
            "author": "Autoria",
            "created_at": "Criado em",
            "image": "URL da Imagem",
            "categories": "Categorias",
        }
        widgets = {
            "title": forms.TextInput(attrs={"type": "text", "id": "id_title"}),
            "content": forms.Textarea(
                attrs={"type": "textarea", "id": "id_content"}
            ),
            "author": forms.Select(attrs={"id": "id_author"}),
            "created_at": forms.DateInput(
                attrs={"type": "date", "id": "id_created_at"}
            ),
            "image": forms.FileInput(attrs={"id": "id_image"}),
            "categories": forms.CheckboxSelectMultiple(
                attrs={"id": "id_categories"}
            ),
        }
