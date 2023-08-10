from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Menu(models.Model):
    name=models.CharField(max_length=30)
    contents=models.CharField(max_length=100)
    price=models.FloatField()
    img=models.ImageField()
    order_state_list = [
        ('not_selected', 'Not Selected'),
        ('starters', 'Starters'),
        ('salads', 'Salads'),
        ('specialty', 'Specialty'),  
        ]
    category=models.CharField(max_length=20,choices=order_state_list, default="not_selected")

    def __str__(self):
        return self.name
    
class Special(models.Model):
    name=models.CharField(max_length=30)
    full_name=models.CharField(max_length=100)
    short_content=models.CharField(max_length=300)
    details=models.CharField(max_length=700)
    img=models.ImageField()

    def __str__(self):
        return self.name

    
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name

class BookTable(models.Model):
    name= models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone_no= models.CharField(max_length=12)
    date=models.DateTimeField(default=datetime.now())
    sits=models.IntegerField(default=1)
    message=models.TextField()

    def __str__(self):
        return f"{self.name}-{self.date}"