from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.TextField()
    long_content = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')

    def get_detail_url(self):
        return reverse('products:detail', args=[self.pk])
