from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
#class customer(models.Model):
 #   acc = models.PositiveIntegerField(primary_key=True)
  #  name = models.CharField(max_length=50)
   # email = models.EmailField(max_length=100,unique=True)
    #balance = models.FloatField()
    #phone = models.PositiveIntegerField()

#class history(models.Model):
 #   sender = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='sender')
  #  receiver = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='receiver')
   # amt = models.FloatField()
    #date= models.DateTimeField(auto_now_add=True)    

class Customer(models.Model):
    sr_no = models.AutoField(primary_key=True)
    acc_no = models.DecimalField(max_digits=5, decimal_places=0)
    name = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=30)
    phone = models.DecimalField(unique=True, max_digits=10, decimal_places=0)
    balance = models.DecimalField(max_digits=8, decimal_places=0)

class History(models.Model):
    sr_no = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=30)
    reciever = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=0)