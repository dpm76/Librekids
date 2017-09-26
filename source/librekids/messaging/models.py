from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    '''
    Message delivered from one use to another user or a group of users.
    System messages uses the admin user account 
    '''
    
    from_user = models.ForeignKey(User, null=False)    
    content_text = models.TextField(blank=False)
    creation_time = models.DateTimeField(null=False)
    delivery_time = models.DateTimeField(null=True)
    is_draft = models.BooleanField()
    parent_message = models.ForeignKey("self", null=True, on_delete=models.CASCADE)
    

class MessageDelivery(models.Model):
    '''
    Message delivery status for each recipient
    '''
    
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField()
