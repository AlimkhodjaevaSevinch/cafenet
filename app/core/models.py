from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from address.models import AddressField
from djmoney.models.fields import MoneyField
from django.db import models

# TODO: Basket model; Order Statuses, Rating, Date, Payment Methods; integrate MoneyField


class CustomUser(AbstractUser):
    addresses = models.ManyToManyField('core.UserAddress', on_delete=models.CASCADE, related_name='users')


class CafeChain(models.Model):
    name = models.CharField(max_length=100)


class Cafe(models.Model):
    cafe_net = models.ForeignKey('core.CafeChain', on_delete=models.CASCADE, related_name='cafes')
    working_hours = models.TimeField()
    address = AddressField()


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = MoneyField(max_digits=7, decimal_places=2, default_currency='BYN')
    description = models.TextField(blank=True)


class Order(models.Model):
    BAD = 'Bad'
    EXCELLENT = 'Excellent'
    RATING_CHOICES = (
        (1, BAD),
        (2, ''),
        (3, ''),
        (4, ''),
        (5, EXCELLENT)
    )
    BY_CARD = 'By card'
    BY_CASH = 'By cash'
    PAYMENT_TYPE_CHOICES = (
        (0, BY_CARD),
        (1, BY_CASH),
    )
    STATUS_CHOICES = (
        (0, ''),
    )
    client = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='Order')
    cafe = models.ManyToManyField('core.Cafe', related_name='orders')
    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT_TYPE_CHOICES)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)


class UserAddress(models.Model):
    address = AddressField()
