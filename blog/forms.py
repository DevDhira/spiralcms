from dataclasses import field, fields
from django import forms
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db  import models

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title' , 'content' , 'excerpt', 'image', 'category', 'urlslug']


class AuthorSignupForm(UserCreationForm):
    email = models.CharField(max_length=500,unique=True)
   # fullname = models.CharField(max_length=500)
    class Meta:
        model  =  User
        fields = ['username','email','password1','password2']
    
    def __init__(self, *args, **kwargs):
        super(AuthorSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out' 
        self.fields['email'].widget.attrs['class'] = 'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out' 
        self.fields['password1'].widget.attrs['class'] = 'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out' 
        self.fields['password2'].widget.attrs['class'] = 'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out' 


