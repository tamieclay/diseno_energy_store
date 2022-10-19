from django.db import models
from .product import Products
from .customer import Customer
import datetime
import uuid


class Order(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    token = models.CharField(max_length=100, blank=True)
    date_ordered =  models.DateField (default=datetime.datetime.today)
    expected_delivery_date = models.DateField (default=datetime.datetime.today)
    transfer_code = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.phone
    
    def save(self, *args, **kwargs):
         if self.token =="":
          self.token = str(uuid.uuid4()).replace("-","").upper()[:10] 
          return super().save(*args,**kwargs)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

