from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import Profile
from django.core.validators import RegexValidator


#Custom user SignUpForm
# ^[A-Za-z]\\w{5, 29}$
# r'^[0-9a-zA-Z]*$'

# ^[a-zA-Z]+([_ -]?[a-zA-Z0-9])*$ ------ recent used regex expression 


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',min_length=8,max_length=15,
                                help_text = '*Use 8-15 charecter',
                                widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password',min_length=8,max_length=15,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    username  = forms.CharField(label='',min_length=6,max_length=30,help_text = '*Do not use special charecter except underscore',
                                validators=[RegexValidator('^[a-zA-Z]+([_ -]?[a-zA-Z0-9])*$', message="Username should be follow characters")],
                                required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username',}))
    first_name = forms.CharField(label='',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label='',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(label='',required=True,
                            help_text = '*Use valid email for verification purpose',
                            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
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
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }


#custom Login Form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control','placeholder':'User Name'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control','placeholder':'Password'}))



class ProfileModelForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['first_name','last_name','institute','facebook_link','linkdin_link','github_link','codeforces_link','website_link','country','bio','avater']