from django import forms
from django.forms import Textarea

from wallOf.models import *


# class Post(forms.Form):
#     title = forms.CharField(required=False)
#     emotion = forms.CharField(required=True, max_length=240, widget=forms.Textarea)

class Posts(forms.ModelForm):
    class Meta:
        model = ModelPosts
        fields = [
            'title',
            'frustration',
            # 'vote',
            # 'date',
        ]
        widgets = {
            'frustration': Textarea(
                attrs={
                    'cols': 100,
                    'rows': 10,
                    'placeholder': 'how was your day',
                    'class': 'input_here form-control',
                    'id': 'main-text',
                },
            ),
            'title': Textarea(
                attrs={
                    'cols': 100,
                    'rows': 2,
                    'placeholder': 'optional',
                    'class': 'input_here form-control',
                }
            )
        }


class Vote_Here(forms.Form):
    # up_down = (
    #     ('vote_here', 'up_vote'),
    #     ('down', 'down_vote'),
    # )
    # myfield = forms.ChoiceField(widget=forms.RadioSelect, choices=up_down)

    CHOICES = [('vote_here', 'vote_here vote'),
               ('down', 'down vote')]

    vote = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    # class Meta:
    #     model = ModelPosts
    #     fields = [
    #         # 'vote'
    #         'up_vote',
    #         'down_vote',
    #     ]

    # widgets = {
    #     'up_vote' : RadioSelect()
    # }


class secretes(forms.ModelForm):
    class Meta:
        model = ModelSecretes
        fields = [
            'title',
            'secrete'
            # 'vote',
            # 'date',
        ]
        widgets = {
            'secrete': Textarea(
                attrs={
                    'cols': 100,
                    'rows': 10,
                    'placeholder': 'tell me...',
                    'class': 'input_here form-control',
                    'id': 'main-text',
                },
            ),
            'title': Textarea(
                attrs={
                    'cols': 100,
                    'rows': 2,
                    'placeholder': 'optional',
                    'class': 'input_here form-control',
                }
            )
        }












class advice(forms.ModelForm):
    class Meta:
        model = ModelAdvice
        fields = [
            'title',
            'advice'
        ]
        widgets = {
            'advice': Textarea(
                attrs={
                    'cols': 100,
                    'rows': 10,
                    'placeholder': 'tell me...',
                    'class': 'input_here form-control',
                    'id': 'main-text'
                },
            ),
            'title': Textarea(
                attrs={
                    'cols': 100,
                    'rows': 2,
                    'placeholder': 'optional',
                    'class': 'input_here form-control',
                }
            )
        }



