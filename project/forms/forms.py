from django import forms
from .models import Inform
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):

    class Meta:
        model = Inform
        fields = ['name', 'description']
        # fields = ['name', 'description', 'category']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     description = cleaned_data.get('description')
    #     if description is not None and len(description) < 20:
    #         raise ValueError({
    #             "description": "Описание не может быть менее 20 символов"
    #         })
    #
    #     name = cleaned_data.get('name')
    #     if name == description:
    #         raise ValidationError(
    #             "Описание не должно быть идентично названию"
    #         )
    #
    #     return cleaned_data