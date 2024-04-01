from django.db import models
from django.contrib.auth.models import User

    
class Category(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    image=models.ImageField(upload_to='images',null=True)
    
    def __str__(self):
        return self.name