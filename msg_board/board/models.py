""" Django Models For Message Board Application """
from django.db import models

# Create your models here.
class Message(models.Model):
    """ Model Message where we store all messages sent by users """
    msg_text = models.CharField(max_length=140, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    msg_source = models.CharField(max_length=25, null=True, blank=True)
    sender_name = models.CharField(max_length=50, null=True, blank=True)
    sender_email = models.EmailField(max_length=50, null=True, blank=True)

    def __str__(self):             
        return str(self.id)

class SecretToken(models.Model):
    """ Secret Token Model """
    token = models.CharField(max_length=50, null=False, blank=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
