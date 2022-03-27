from django.db import models
from django.conf import settings
from django.utils import timezone
from user.models import User
from django.db.models import Sum
from django.urls import reverse



BREAKTIME = 1
LUNCHTIME = 2

ORDER_TIMES = (
    (BREAKTIME, 'Breaktime'),
    (LUNCHTIME, 'Lunchtime')

)



# Create your models here.

class FoodItem(models.Model):
    name = models.CharField(max_length =60)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)
    availability = models.BooleanField(default = True)
    description = models.CharField(max_length = 60)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    item = models.ForeignKey(FoodItem, on_delete = models.CASCADE, null = True, blank = True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0)


    def __str__(self):
        return self.item.name

    def get_total_item_price(self):
        self.price =  self.quantity * self.item.price
        

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=4, decimal_places=2, default = 0)
    order_items = models.ManyToManyField(OrderItem)
    is_completed = models.BooleanField(default = False)
    deliver_by = models.CharField(max_length = 1, choices = ORDER_TIMES, default = BREAKTIME)


    def total_sum(self):
        self.total =  sum(order_item.price * order_item.quantity for order_item in self.order_items.all())

