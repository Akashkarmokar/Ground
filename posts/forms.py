from django import forms
from .models import Post,Comment


class PostModelForm(forms.ModelForm):
    heading = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control heading-form','rows':'1','placeholder':'Heading...'}))
    link = forms.CharField(required=False,label='',widget=forms.Textarea(attrs={'class':'form-control link-form','rows':'3','placeholder':'Your Problem Link'}))
    content = forms.CharField(label='',widget=forms.Textarea(attrs={'rows':'3','placeholder':'What is on your mind...'}))
    image = forms.ImageField(required=False,label='',widget=forms.FileInput(attrs={'class':'file-upload-field','id':'actual-btn'}))
    class Meta:
        model = Post
        fields = ['heading','link','content','image']


class CommentModelForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'class':'form-control commentText','placeholder':'Write a comment'}),
    )
    class Meta:
        model = Comment
        fields = ['body',]