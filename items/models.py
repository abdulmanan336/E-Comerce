from django.db import models
import uuid
# Create your models here.

class Special(models.Model):
    title = models.CharField(max_length=250)
    offer = models.PositiveSmallIntegerField(default=0)
    overview = models.CharField(max_length=50)
    img = models.ImageField(upload_to='items/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    


class Brand(models.Model):
    title = models.CharField(max_length=80)
    thumbnail = models.ImageField(upload_to='items/thumbnails', null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=80)
    brands = models.ManyToManyField(Brand)
    thumbnail = models.ImageField(upload_to='items/thumbnails', null=True, blank=True)
    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.title

class Item(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='items', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    offer = models.ForeignKey(Special, on_delete=models.SET_NULL,null=True, blank=True)
    title = models.CharField(max_length=300)
    overview = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='items/thumbnails', null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField(default=0)
    discount = models.PositiveSmallIntegerField(default=0)
    featured = models.BooleanField()


    free_shipping = models.BooleanField(default=True)
    shipping_price = models.PositiveSmallIntegerField(default=0)
    min_shipping = models.PositiveSmallIntegerField(default=3)
    max_shipping = models.PositiveSmallIntegerField(default=10)
    delivery = models.PositiveSmallIntegerField(default=4)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    @property
    def get_discount_price(self):
        return self.sale_price * self.discount / 100
    
    @property
    def get_discounted_price(self):
        return self.sale_price - self.sale_price * self.discount / 100

class Image(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='items/images')
    order = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.item.title
    
class Stock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,)
    quantity = models.PositiveSmallIntegerField(default=0)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        item = self.item
        item.quantity += self.quantity
        item.save()
        super().save(*args, **kwargs)

    
    