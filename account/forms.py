from django import forms

class registerForm(forms.Form):
    name = forms.CharField(label='Name :', max_length=100 ,required=True)
    family = forms.CharField(label='Family :', max_length=100 ,required=True)
    email = forms.EmailField(label='Email :', max_length=100 ,required=True)
    username = forms.CharField(label='User Name :', max_length=100 ,required=True)
    password = forms.CharField(label='Password :', max_length=100,widget=forms.PasswordInput() ,required=True)
    
