from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from Pizza_Django_Framework.accounts.models import PizzaUser
from Pizza_Django_Framework.pizza.models import Pizza

UserModel = get_user_model()


# Create your models here.
# class Customer(models.Model): #tova ni e user-a
#user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
# name = models.CharField(max_length=200, null=True)
# email = models.CharField(max_length=200)

# def __str__(self):
#    return self.name

# class Product(models.Model): #tova e pizzata
# name = models.CharField(max_length=200)
# price =models.FloatField()
# digital =models.BooleanField(default=False, null=True, blank=True)
# image

# def __str__(self):
#    return self.name

class Order(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.pizza.price * self.quantity
        return total


class ShippingAddress(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    # customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
