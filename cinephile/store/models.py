from django.db import models
from django.contrib.auth.models import User

    
class Category(models.Model):
    name=models.CharField(max_length=50,null=False)
    discription=models.TextField(max_length=600,null=True)
    
    def __str__(self):
        return self.name
    

    
class Item(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)    
    title=models.CharField(max_length=50,null=False)
    image=models.ImageField(upload_to='images',null=True)
    genre=models.CharField(max_length=50,null=False)
    release_date=models.CharField(max_length=20,null=False)
    duration=models.CharField(max_length=20,null=False)
    summary=models.TextField(max_length=700,null=False)
    language=models.CharField(max_length=50,null=False)
    director=models.CharField(max_length=50,null=False)
    writter=models.CharField(max_length=50,null=False)
    leadrole=models.CharField(max_length=50,null=False)
    actor1=models.CharField(max_length=50,null=True)
    actor2=models.CharField(max_length=50,null=True)
    actor3=models.CharField(max_length=50,null=True)
    actor4=models.CharField(max_length=50,null=True)
    actor5=models.CharField(max_length=50,null=True)
    seasons=models.IntegerField(null=True)
    episodes=models.IntegerField(null=True)

    def __str__(self):
        return self.title
    

