from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    contact_picture = models.URLField(null=True)
    is_favorite = models.BooleanField(default=False)
