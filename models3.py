# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    sr_no = models.AutoField(primary_key=True)
    acc_no = models.DecimalField(max_digits=5, decimal_places=0)
    name = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=30)
    phone = models.DecimalField(unique=True, max_digits=10, decimal_places=0)
    balance = models.DecimalField(max_digits=8, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'customer'


class History(models.Model):
    sr_no = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=30)
    reciever = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'history'
