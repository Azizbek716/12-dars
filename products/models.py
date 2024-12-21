from django.db import models
from django.shortcuts import reverse


class Products(models.Model):
    objects = None
    product_lis = models.CharField(max_length=100)
    product_detail = models.DateField(auto_now_add=True)
    product_create = models.CharField(max_length=100)
    about_page = models.TextField()

    def get_detail_url(self):
        return reverse('products:detail', args=[self.pk])
