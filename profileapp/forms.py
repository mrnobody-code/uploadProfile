from django import forms 
from .models import *

class ProfileForm(forms.ModelForm):
    # TODO: Define form fields here
    class Meta:
    	model = Profile
    	fields ='__all__'