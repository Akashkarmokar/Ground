from django import forms
from .models import Domain,Solution



class DomainModelForm(forms.ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','rows':'1','placeholder':'Type Domain Name'}))
    class Meta:
        model = Domain
        fields = ['name',]


class SolutionModelForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['domain','number','link',]