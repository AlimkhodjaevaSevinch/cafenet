from django.contrib.auth.models import AbstractUser
from address.models import AddressField
from django.db import models


class CustomUser(AbstractUser):
    client_groups = models.ManyToManyField('core.Order', related_name='Client')


class Cafe(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey('core.Food', on_delete=models.CASCADE, related_name='Cafe')
    style = models.CharField(max_length=100)
    working_hours = models.TimeField()
    address = AddressField()


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(blank=True)


class Order(models.Model):
    client_name = models.ForeignKey('core.CustomUser',on_delete=models.CASCADE,related_name='Order')
    cafe_name = models.ManyToManyField('core.Cafe', related_name='Order')
    payment_method = models.CharField(max_length=50)
    address_dostavki = AddressField()


class Delivery(models.Model):
    operating_mode = models.TimeField()
    shipping_cost = models.SmallIntegerField()
