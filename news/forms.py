from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'maxlength': '200',
                'required': 'required'
            })
        }


# class NewsForm(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = ['title', 'content', 'author', 'created_at',
# 'image', 'categories']
#         widgets = {
#             'categories': forms.CheckboxSelectMultiple(),
#             'author': forms.Select()
#         }
