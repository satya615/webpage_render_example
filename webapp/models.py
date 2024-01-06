from django.db import models

# Create your models here.
class Userlogin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
class booking(models.Model):
    username=models.CharField(max_length=100)
    num=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    
class Menu(models.Model):
    num=models.CharField(max_length=100)
    items=models.CharField(max_length=100)
    item_type=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

class Order(models.Model):
    username=models.CharField(max_length=100)
    items=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    count=models.IntegerField()
    status=models.CharField(max_length=100)
class Logindetails(models.Model):
    username=models.CharField(max_length=100)
    Date=models.DateTimeField()