import email
from pyexpat import model
from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField( max_length=122) 
    phone= models.CharField(max_length=12)
    desc= models.TextField()
    date= models.DateField()
 
    def __str__(self):
        return self.name
class Pro(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    desc= models.TextField()

    
    def __str__(self):
        return self.name