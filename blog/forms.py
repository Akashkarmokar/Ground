from django import forms
from .models import Blog,blogComment,Category
from ckeditor.fields import RichTextField

class CategoryModelForm(forms.ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Create a new category'}))
    class Meta:
        model = Category
        fields = ['name',]        


class CreateBlogModelForm(forms.ModelForm):
    title = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control heading-form','rows':'1','placeholder':'Title'}))
    class Meta:
        model = Blog
        fields = ['title','category','content']
        
class blogCommentModalForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'class':'form-control'})
    )
    class Meta:
        model = blogComment
        fields = ['body']
