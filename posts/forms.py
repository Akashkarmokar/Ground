from django import forms
from .models import Post,Comment


class PostModelForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.Textarea(attrs={'rows':'3','placeholder':'What is on your mind...'}))
    image = forms.ImageField(label='',widget=forms.FileInput(attrs={'class':'file-upload-field','id':'actual-btn'}))
    class Meta:
        model = Post
        fields = ['content','image']


class CommentModelForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Write a comment'}),
    )
    class Meta:
        model = Comment
        fields = ['body',]