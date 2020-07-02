from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CreateArticleForm(forms.Form):
    header = forms.CharField(
                        max_length=100,
                        widget=forms.TextInput(
                            attrs={
                                'class': 'form-control',
                                'type': 'text',
                                'aria-label': 'Large',
                                'aria-describedby': 'inputGroup-sizing-sm',
                                }
                        )
                    )
    text = forms.CharField(widget=SummernoteWidget())

    FEED_SECTIONS = [
        ('WS', 'Водогосподарська обстановка'),
        ('EV', 'Еколого-просвітницькі заходи'),
        ('MR', 'Управління річковими басейнами'),
    ]
    category = forms.ChoiceField(
        choices=FEED_SECTIONS,
        widget=forms.Select(
            attrs={
                'class': "custom-select",
                'for': "CategorySelect",
            }
        )
    )

    # def clean(self):
    #     cleaned_data = super(CreateArticleForm, self).clean()
    #     header = cleaned_data.get('header')
    #     text = cleaned_data.get('text')
    #     category = cleaned_data.get('category')
    #     if not name and not email and not message:
    #         raise forms.ValidationError('You have to write something!')