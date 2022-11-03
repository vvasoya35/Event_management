from dataclasses import field
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from Event_Management import settings
class ServicesForm(ModelForm):
    class Meta:
        model = Event_Services
        fields = ['service_owner','service_name','service_description','category','price','featured_image']
        
    def __init__(self,*args, **kwargs):
        super(ServicesForm, self).__init__(*args, **kwargs)
    
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control required'})    
            
        self.fields['featured_image'].widget.attrs.update({'class':'file-upload-browse btn btn-gradient-primary', 'placeholder':'Upload Image'})
        self.fields['category'].widget.attrs.update({'class':'form-control form-control-sm', 'placeholder':'Upload Image'})
        

class ServiceBookForm(ModelForm):
    # date_time = forms.SplitDateTimeField(widget=AdminSplitDateTime())
    class Meta:
        model = booking
        fields = [
            'address',
            'start_date',
            'end_date',
            # 'start_time',
            # 'end_time'
            ]
        

        # widgets = {
        #     'start_date': AdminDateWidget(),
        #     'end_date': AdminDateWidget(),
        #     'start_time': AdminTimeWidget(),
        #     'end_time': AdminTimeWidget(),
        # }

        
    def __init__(self,*args,**kwargs):
        super(ServiceBookForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control required','placeholder':name})   
        
        # print(self.fields['start_date'].DateInput)
        self.fields['start_date'].widget.attrs.update({'class':'form-control col-md-6 required datepicker'})
        self.fields['end_date'].widget.attrs.update({'class':'form-control col-md-6 required datepicker'})
        
        # self.fields['start_time'].widget.attrs.update({'class':'form-control col-md-6 required timepicker'})
        
        # self.fields['end_time'].widget.attrs.update({'class':'form-control col-md-6 required timepicker'})
        