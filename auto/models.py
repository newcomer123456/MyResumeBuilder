from django.db import models
from django.contrib.auth.models import Permission, AbstractUser
from django.contrib.contenttypes.models import ContentType

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(max_length=342, null=True, blank=True)
    foto = models.ImageField(upload_to='user_foto/',null=True, blank=True)
    
    role = models.CharField(max_length=20, choices=[
        ('user', 'User'),
        ('admin', 'Admin'),
    ])