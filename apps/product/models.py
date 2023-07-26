from django.db import models
from apps.vendor.models import Vendor
import os, datetime

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join("uploads/", filename)


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    price = models.IntegerField()
    quantity = models.IntegerField()
    small_description = models.TextField(max_length=150)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=get_file_path, height_field=None, width_field=None, max_length=None)
