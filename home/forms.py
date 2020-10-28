from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content',]
        labels = {
            'content':'Feedback',
        }
        widgets = {
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Type here your valuable feedback'}),
        }