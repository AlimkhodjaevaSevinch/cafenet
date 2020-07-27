from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from address.models import AddressField
from djmoney.models.fields import MoneyField
from django.db import models

# TODO: Basket model; Order Statuses, Rating, Date, Payment Methods; integrate MoneyField


class CustomUser(AbstractUser):
    addresses = models.ManyToManyField('core.UserAddress', on_delete=models.CASCADE, related_name='users')
    foods = models.ManyToManyField('core.Food', related_name='users', through='core.Basket')


class CafeChain(models.Model):
    name = models.CharField(max_length=100)


class Cafe(models.Model):
    cafe_net = models.ForeignKey('core.CafeChain', on_delete=models.CASCADE, related_name='cafes')
    working_on = models.TimeField()
    working_off = models.TimeField()
    address = AddressField()


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = MoneyField(max_digits=7, decimal_places=2, default_currency='BYN')
    description = models.TextField(blank=True)


class Order(models.Model):
    AWFUL = 1
    BAD = 2
    NORMAL = 3
    GOOD = 4
    EXCELLENT = 5

    RATING_CHOICES = (
        (AWFUL, 'Awful'),
        (BAD, 'Bad'),
        (NORMAL, 'Normal'),
        (GOOD, 'Good'),
        (EXCELLENT, 'Excellent')
    )
    BY_CARD = 0
    BY_CASH = 1
    PAYMENT_TYPE_CHOICES = (
        (BY_CARD,'By card'),
        (BY_CASH,'By cash'),
    )
    ORDER_IS_ACCEPTED = 0 #заказ принят
    PREPARE = 1 #готовиться
    ORDER_IS_READY = 2 #заказ готов
    ORDER_IN_TRANSIT = 3 #заказ в пути
    ORDER_DELIVERED = 4 #заказ доставлен
    STATUS_CHOICES = (
        (ORDER_IS_ACCEPTED, 'Order is accepted'),
        (PREPARE, 'Prepare'),
        (ORDER_IS_READY, 'Order is ready'),
        (ORDER_IN_TRANSIT, 'Order in transit'),
        (ORDER_DELIVERED, 'Order delivered')
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    cafe = models.ManyToManyField('core.Cafe', related_name='orders')
    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT_TYPE_CHOICES)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    date = models.DateTimeField()
    status = models.PositiveSmallIntegerField()



class UserAddress(models.Model):
    address = AddressField()


class Basket(models.Model):
    foods = models.ForeignKey('core.Food', on_delete=models.CASCADE, related_name='baskets')
    user = models.ForeignKey('core.CustomUser', on_delete=models.CASCADE, related_name='basket')
    quantity = models.PositiveSmallIntegerField()