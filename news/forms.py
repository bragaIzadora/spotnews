from django import forms
from .models import Category, News


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


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content',
                  'author', 'created_at', 'image', 'categories']
        widgets = {
            'title': forms
            .TextInput(attrs={'maxlength': '200', 'required': 'required'}),
            'content': forms
            .Textarea(attrs={'required': 'required'}),
            'created_at': forms
            .DateInput(attrs={'type': 'date', 'required': 'required'}),
        }
