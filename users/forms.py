from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import Profile
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[a-zA-Z]+([_ -]?[a-zA-Z0-9])*$')


#Custom user SignUpForm
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    username = forms.CharField(label='', validators=[alphanumeric],required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
        }
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
        }


#custom Login Form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control','placeholder':'User Name'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control','placeholder':'Password'}))



class ProfileModelForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['first_name','last_name','institute','facebook_link','linkdin_link','github_link','codeforces_link','website_link','country','bio','avater']