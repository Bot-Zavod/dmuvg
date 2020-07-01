from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class CreateArticleForm(forms.Form):
    header = forms.CharField(max_length=100)
    text = forms.CharField(widget=SummernoteWidget())
    category = forms.CharField(max_length=100)

    # def clean(self):
    #     cleaned_data = super(CreateArticleForm, self).clean()
    #     header = cleaned_data.get('header')
    #     text = cleaned_data.get('text')
    #     category = cleaned_data.get('category')
    #     if not name and not email and not message:
    #         raise forms.ValidationError('You have to write something!')