from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    middle_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    contact = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    
    
@receiver(post_save, sender=User)
def create_User_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(User=instance)
        
        