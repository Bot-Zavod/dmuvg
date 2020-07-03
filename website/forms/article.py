from django import forms

from django_summernote.widgets import SummernoteWidget

from website.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("header", "text", "category")
        FEED_SECTIONS = [
            ('WS', 'Водогосподарська обстановка'),
            ('EV', 'Еколого-просвітницькі заходи'),
            ('MR', 'Управління річковими басейнами'),
        ]
        widgets = {
            'header': forms.TextInput(
                            attrs={
                                'class': 'form-control',
                                'type': 'text',
                                'aria-label': 'Large',
                                'aria-describedby': 'inputGroup-sizing-sm',
                                }
                        ),

            'category': forms.Select(
                            attrs={
                                'default': 'WS',
                                'choices': FEED_SECTIONS,
                                'class': "custom-select",
                                'for': "CategorySelect",
                            }
                        ),

            'text': SummernoteWidget(),
        }
