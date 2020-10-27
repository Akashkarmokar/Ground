from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','email','mobileNo','content']
        labels = {
            'name':'Name',
            'email':'Email',
            'mobileNo':'Contact No',
            'content':'Feedback',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'mobileNo':forms.TextInput(attrs={'class':'form-control','placeholder':'Contact NO'}),
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Type here your valuable feedback'}),
        }