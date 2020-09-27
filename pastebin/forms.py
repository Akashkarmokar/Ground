from django.core import validators
from django import forms
from . models import Pastebindb # here i import my database table 



poster_type_choice = (
    ('none','None'),
    ('c','C'),
    ('cpp','C++'),
    ('py','Python'),
    ('java','Java'),
)


class pasteFm(forms.ModelForm):
    poster_type = forms.ChoiceField(choices=poster_type_choice)
    class Meta:
        model = Pastebindb
        fields = ['poster_name','poster_type','poster']
        labels = {
            'poster_name':'Poster Name',
            'poster_type':'Syntax ',
            'poster':'Content ',
        }
        widgets = {
            'poster':forms.Textarea(
                attrs={'rows':'15','cols':'150'}
            ),
        }