from django.db import models
import uuid
from users.models import profile
from services.models import Event_Services
# from .models import messageTo
# Create your models here.
class messageTo(models.Model):
    mess_receiver = models.ForeignKey(profile,on_delete=models.SET_NULL,null=True,related_name="messages")
    mess_sender = models.ForeignKey(profile,on_delete=models.SET_NULL,null=True)
    mess_service = models.ForeignKey(Event_Services,on_delete=models.CASCADE,null=True,blank= True)
    message = models.TextField(null=True,blank= True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    # reply_id = models.UUIDField(default=uuid.uuid4,null=True,blank=True)
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    class Meta:
        ordering = ['-created']
    