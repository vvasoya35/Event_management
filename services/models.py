from email.policy import default
from random import choice, choices
from django.db import models
import uuid
from Event_Management import settings
from django.contrib.auth.models import User
from users.models import *
# Create your models here.
class Event_Services(models.Model):
    service_owner=models.ForeignKey(profile,on_delete=models.CASCADE,null=True,blank=True)

    service_name = models.CharField(max_length=200)
    service_description = models.TextField()
    category = models.ForeignKey('Service_Category',on_delete= models.CASCADE, null=True, blank=True)
    featured_image = models.ImageField(null=True,blank=True,default="default.jpg")
    price = models.IntegerField(null=True,blank=True)
    
    
    vote_total = models.IntegerField(default=0,null=True, blank=True)
    vote_ratio = models.IntegerField(default=0,null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.service_name
    
class Service_Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.category_name
    
    
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(profile, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Event_Services, on_delete=models.CASCADE)
    # service = models.ForeignKey(Event_Services, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    # class Meta:
    #     unique_together = [['owner','project']]
    
    def __str__(self):
        return self.value
    
class booking(models.Model):
    book_status = (
        ('Processing', 'Processing'),
        ('Accept', 'Accept'),
        ('Running', 'Running'),
        ('Completed', 'Completed'),
    )
    customer = models.ForeignKey(profile,on_delete=models.CASCADE, null=True, blank=True)
    services = models.ForeignKey(Event_Services,on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    start_date = models.DateField(auto_now_add=False,auto_now=False,null=True, blank=True)
    end_date = models.DateField(auto_now_add=False,auto_now=False,null=True, blank=True)
    start_time = models.TimeField(auto_now_add=False,auto_now=False,null=True, blank=True)
    end_time = models.TimeField(auto_now_add=False,auto_now=False,null=True, blank=True)
    status = models.CharField(max_length=200,choices=book_status,default='Processing')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)