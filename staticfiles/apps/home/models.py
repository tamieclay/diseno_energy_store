# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse
from store.models import Customer


# Create your models here.
''' class Customer(models.Model):
 user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
 name = models.CharField(max_length=200, null=True)
 email = models.CharField(max_length=200) '''
 
class Meta:
        verbose_name = ('Customer')
        verbose_name_plural = ('Customer')
        
class MainProducts(models.Model):
     products_image = models.ImageField(upload_to='media')
     ''' product_thumbnail = ImageSpecField(source='products_image',
                            processors=[ResizeToFill(200,200)],
                                  format='PNG', 
                                  options={'quality':60} , blank=True) '''
     products_video = models.FileField(upload_to='media/%y',blank=True)
     product_title = models.CharField(max_length=200)
     product_desc = models.CharField(max_length=600)
     product_spec1 = models.CharField(max_length=600)
     product_spec2 = models.CharField(max_length=600)
     product_spec3 = models.CharField(max_length=600)
     product_price = models.DecimalField(max_digits=7, decimal_places=2)
     
     def _str_(self):
         return self.product_title
 
class Meta:
        verbose_name = ('MainProducts')
        verbose_name_plural = ('MainProducts') 
        
        
        
class FeaturedProducts(models.Model):
      main_products_image = models.ImageField(upload_to='media', blank=True)
      products_image1 = models.ImageField(upload_to='media', blank=True)
      products_image2 = models.ImageField(upload_to='media', blank=True)
      products_image3 = models.ImageField(upload_to='media', blank=True)
      ''' product_thumbnail = ImageSpecField(source='products_image',
                            processors=[ResizeToFill(200,200)],
                                  format='PNG', 
                                  options={'quality':60} , blank=True) '''
      product_title = models.CharField(max_length=200)
      product_desc = models.CharField(max_length=600)
      product_price = models.DecimalField(max_digits=5, decimal_places=2)
     
      def _str_(self):
         return self.product_title
     
      def get_absolute_url(self):
        	 return reverse("apps.home:shop", kwargs={"pk": self.pk})
 
 
class Meta:
        verbose_name = ('Customer')
        verbose_name_plural = ('Customer')                 
        
        
 
 




''' class Order(models.Model):
 customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
 date_ordered = models.DateTimeField(auto_now_add=True)
 expected_delivery_date = models.DateTimeField()
 complete = models.BooleanField(default=False)
 token = models.CharField(max_length=100, blank=True)
 
 
 def _str_(self):
     return self.token
 
#  def __str__(self):
#         return f"{self.customer}-{self.token}"
    
 class Meta:
        ordering = ['customer']   
    
 def save(self, *args, **kwargs):
     if self.token =="":
         self.token = str(uuid.uuid4()).replace("-","").upper()[:10] 
     return super().save(*args,**kwargs)  
 
 def get_absolute_url(self):
    	 return reverse("apps.home:order-detail", kwargs={"pk": self.pk}) '''
 
    


