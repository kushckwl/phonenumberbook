from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=30, null=True, blank=True)
    number = models.CharField(max_length=12)
    date_added = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.name