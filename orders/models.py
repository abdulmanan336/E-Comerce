from django.db import models
from items.models import Item
# Create your models here.

class Order(models.Model):
    order_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    
    
    
    sub_total = models.PositiveSmallIntegerField(default=0)
    sub_shipping = models.PositiveSmallIntegerField(default=0)

    order_processing = models.BooleanField(default=True)
    order_placed = models.BooleanField(default=False)
    order_shipping = models.BooleanField(default=False)
    order_deliverd = models.BooleanField(default=False)
    order_rejected = models.BooleanField(default=False)
    order_poked = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name
    
    @property
    def status(self):
        current_status = 'order_placed'
        if self.order_processing:
            current_status = 'order_processing'
        if self.order_shipping:
            current_status = 'order_shipping'
        if self.order_deliverd:
            current_status = 'order_deliverd'
        if self.order_rejected:
            current_status = 'order_rejected'
        if self.order_poked:
            current_status = 'order_poked'
        return current_status
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.PositiveSmallIntegerField(default=1)
    sale_price = models.PositiveSmallIntegerField()
    discount = models.PositiveSmallIntegerField()
    shipping_price = models.PositiveSmallIntegerField()

    return_requested = models.BooleanField(default=False)
    return_note = models.CharField(max_length=550, blank=True, null=True)
    returned = models.BooleanField(default=False)
    
    @property
    def get_discount_price(self):
        return self.sale_price * self.discount / 100
    
    @property
    def get_discounted_price(self):
        return self.sale_price - self.sale_price * self.discount / 100
