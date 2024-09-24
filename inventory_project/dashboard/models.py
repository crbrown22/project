from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('T-shirt','T-shirt'),
    ('Hoodie','Hoodie'),
    ('Shorts','Shorts'),
    ('Joggers','Joggers'),
    ('Socks','Socks'),
    ('Supplements','Supplements'),
    ('Programs','Programs'),
    ('Subscription','Subscription')
)
class Product (models.Model):
    name = models.CharField(max_length=100, null=True)
    category= models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveBigIntegerField(null=True)

    def __str__(self):
        return (f'{self.name}')

    class Meta:
        verbose_name_plural='Customer Product'


class Order(models.Model):
    product =models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, models.CASCADE,null=True )
    order_quantity = models.PositiveIntegerField(null=True)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.customer}: {self.order_quantity} - {self.product} / {self.date}')

    class Meta:
        verbose_name_plural='Customer Order'