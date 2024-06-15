from django.db import models
from items.models import Item
from accounts.models import User

class OrderStatus(models.Model):
    ORDER_STATUS = (
        ('order_placed', 'order_placed'),
        ('paid', 'paid'),
        ('canceled', 'canceled'),
        ('sent', 'sent'),
        )
    
    status_name = models.CharField(choices=ORDER_STATUS)

class CustomerOrder(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False) 
    order_time = models.DateTimeField(auto_now_add=True)
    order_status_id = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
    time_paid = models.DateTimeField(default=None, null=True)
    time_canceled = models.DateTimeField(default=None, null=True)
    time_completed = models.DateTimeField(default=None, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=False)
    
class OrderItem(models.Model):
    customer_order_id = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, null=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

