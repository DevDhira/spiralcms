from django import forms
from .models import AuthorProfile



class AuthorProfileForm(forms.ModelForm):
     class Meta:
        model  =  AuthorProfile
        fields = ['firstname','lastname','location','current_role','about']
    
   #   def __init__(self, *args, **kwargs):
   #      super(AuthorProfileForm, self).__init__(*args, **kwargs)
   #      self.fields['username'].widget.attrs['class'] = 'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out' 
   #      self.fields['email'].widget.attrs['class'] = 'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out' 
   #      self.fields['password1'].widget.attrs['class'] = 'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out' 
   #      self.fields['password2'].widget.attrs['class'] = 'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out' 


