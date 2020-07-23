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
    AWFUL = 'Awful' #ужасно
    BAD = 'Bad'
    NORMAL = 'Normal'
    GOOD = 'Good'
    EXCELLENT = 'Excellent'

    RATING_CHOICES = (
        (1, AWFUL),
        (2, BAD),
        (3, NORMAL),
        (4, GOOD),
        (5, EXCELLENT)
    )
    BY_CARD = 'By card'
    BY_CASH = 'By cash'
    PAYMENT_TYPE_CHOICES = (
        (0, BY_CARD),
        (1, BY_CASH),
    )
    ORDER_IS_ACCEPTED = 'Order is accepted' #заказ принят
    PREPARE = 'Prepare' #готовиться
    ORDER_IS_READY = 'Order is ready' #заказ готов
    ORDER_IN_TRANSIT = 'Order in transit' #заказ в пути
    ORDER_DELIVERED = 'Order delivered' #заказ доставлен
    STATUS_CHOICES = (
        (0, ORDER_IS_ACCEPTED),
        (1, PREPARE),
        (2, ORDER_IS_READY),
        (3, ORDER_IN_TRANSIT),
        (4, ORDER_DELIVERED)
    )
    client = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='order')
    cafe = models.ManyToManyField('core.Cafe', related_name='orders')
    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT_TYPE_CHOICES)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    date = models.DateTimeField()


class UserAddress(models.Model):
    address = AddressField()


class Basket(models.Model):
    foods = models.ManyToManyField('core.Food', related_name='basket')