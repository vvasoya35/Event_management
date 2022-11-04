from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        
        
    def __init__(self,*args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control required','placeholder':field.label})    
            
        # self.fields['featured_image'].widget.attrs.update({'class':'file-upload-browse btn btn-gradient-primary', 'placeholder':'Upload Image'})
        # self.fields['category'].widget.attrs.update({'class':'form-control form-control-sm', 'placeholder':'Upload Image'})
        
class CustomerForm(ModelForm):
    class Meta:
        model = profile
        fields = ['first_name','last_name','username','profile_image','location','Address']
    
    
    def __init__(self,*args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
    
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control required'})    
        self.fields['profile_image'].widget.attrs.update({'class':'file-upload-browse btn btn-gradient-primary', 'placeholder':'Upload Image'})    


class ServiceProviderForm(ModelForm):
    class Meta:
        model = profile
        fields = ['first_name','last_name','profile_image','username','short_intro','bio','email','featured_image','location','Address','GST_Number','Shop_Name','featured_image']
    
    
    def __init__(self,*args, **kwargs):
        super(ServiceProviderForm, self).__init__(*args, **kwargs)
    
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control required'})    
        # self.fields['profile_image'].widget.attrs.update({'class':'file-upload-browse btn btn-gradient-primary', 'placeholder':'Upload Image'})    
