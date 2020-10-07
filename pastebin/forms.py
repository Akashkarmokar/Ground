from django.core import validators
from django import forms
from . models import Pastebindb # here i import my database table 



poster_type_choice = (
    ('none','None'),
    ('markup','Atom'),
    ('c','C'),
    ('cpp','C++'),
    ('css','CSS'),
    ('go','Go'),
    ('git','Git'),
    ('markup','HTML'),
    ('js','JavaScript'),
    ('java','Java'),
    ('javadoc','JavaDoc'),
    ('javadoclike','JavaDoc-like'),
    ('javastacktrace','Java stack trace'),
    ('jq','JQ'),
    ('jsdoc','JSDoc'),
    ('js-extras','JS Extras'),
    ('json','JSON'),
    ('json5','JSON5'),
    ('jsonp','JSONP'),
    ('kotlin','Kotlin'),
    ('kt','Kotlin(kt)'),
    ('kts','Kotlin(kts)'),
    ('livescript','LiveScript'),
    ('markup','Markup'),
    ('markup','Mathml'),
    ('mongodb','MongoDB'),
    ('matlab','MATLAB'),
    ('py','Python'),
    ('powershell','PowerShell'),
    ('processing','Processing'),
    ('pug','Pug'),
    ('perl','Perl'),
    ('php','PHP'),
    ('phpdoc','PHPDoc'),
    ('r','R'),
    ('markup','SVG'),
    ('markup','SSML'),
    ('scheme','Scheme'),
    ('sql','SQL'),
    ('swift','Swift'),
    ('vim','vim'),
    ('markup','XML'), 
)


class pasteFm(forms.ModelForm):
    poster_type = forms.ChoiceField(
        choices=poster_type_choice,
        help_text=" Select one to syntax highlight otherwise code will be considered as plain-text.",
    )
    class Meta:
        model = Pastebindb
        fields = ['poster_name','poster_type','poster']
        labels = {
            'poster_name':'Poster Name',
            'poster_type':'Syntax ',
            'poster':'Content ',
        }
        widgets = {
            'poster_name':forms.TextInput(
                attrs={'class':'form-group'}
            ),
            'poster':forms.Textarea(
                attrs={'class':'form-control','rows':'15','cols':'150'}
            ),
        }