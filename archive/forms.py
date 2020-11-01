from django import forms
from .models import Domain,Solution



class DomainModelForm(forms.ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','rows':'1','placeholder':'Type Domain Name'}))
    class Meta:
        model = Domain
        fields = ['name',]


class SolutionModelForm(forms.ModelForm):
    number = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','rows':'1','placeholder':'Type Problem Number'}))
    link = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','rows':'1','placeholder':'Paste Link Here'}))
    class Meta:
        model = Solution
        fields = ['domain','number','link',]