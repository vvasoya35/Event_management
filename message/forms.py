from dataclasses import fields
from django.forms import ModelForm
from django import forms
from .models import messageTo

class messageToForm(ModelForm):
    class Meta:
        model = messageTo
        fields = ['subject','message']

    def __init__(self,*args,**kwargs):
        super(messageToForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control required'})