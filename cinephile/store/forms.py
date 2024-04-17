from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from store.models import Diary

class RegForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control text-center","style":"height:50px","placeholder":"Username"}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control text-center","style":"height:50px","placeholder":"Firstname"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control text-center","style":"height:50px","placeholder":"Lastname"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control text-center","style":"height:50px","placeholder":"Email"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control text-center","style":"height:50px","placeholder":"Password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control text-center","style":"height:50px","placeholder":"Confirm Password"}))
    
    class Meta:
        model=User
        fields= ["username","first_name","last_name","email","password1","password2"]



class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
    



