from django import forms
from .models import Posts

class post_creation(forms.ModelForm):
    class Meta:
        model=Posts
        fields=[
            'title',
            'content',
            'image'
        ]


class signup_form(forms.Form):
    username=forms.CharField(max_length=150)        
    email=forms.EmailField(max_length=50,required=True)        
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)       

class login_form(forms.Form):
    username=forms.CharField(max_length=150)                
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)       


