from django.db import models
from django.contrib.auth.models import User

    
class Category(models.Model):
    name=models.CharField(max_length=50,null=False)
    discription=models.TextField(null=True)
    
    def __str__(self):
        return self.name
    

    
class Item(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)    
    title=models.CharField(max_length=50,null=False)
    image=models.ImageField(upload_to='images',null=True)
    genre=models.CharField(max_length=50,null=False)
    release_date=models.CharField(max_length=20,null=False)
    duration=models.CharField(max_length=20,null=False)
    summary=models.TextField(null=False)
    language=models.CharField(max_length=50,null=False)
    director=models.CharField(max_length=50,null=False)
    writer=models.CharField(max_length=50,null=False)
    cast=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.title 


