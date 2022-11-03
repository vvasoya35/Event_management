from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    Profile_Type=(
        ('Supplier','Supplier'),
        ('Consumer','Consumer'),
    )
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    role = models.CharField(max_length=200, choices=Profile_Type,blank=True,null=True)
    short_intro = models.CharField(max_length=200,blank=True,null=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/', default="profiles/user-default.png")
    bio = models.TextField(blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    location = models.CharField(max_length=150,blank=True,null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    
    
    GST_Number = models.CharField(max_length=100,blank=True,null=True)
    Shop_Name = models.CharField(max_length=200,blank=True,null=True)
    
    is_active = models.BooleanField(default=False)
    
    Address = models.TextField(blank=True,null=True)
    featured_image = models.ImageField(null=True, blank=True, upload_to="service-images/")
    
    def __str__(self):
        return str(self.first_name)
    
    @property
    def user_name(self):
        username = owner.user.username
