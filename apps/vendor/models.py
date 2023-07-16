from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join("uploads/", filename)


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    shop_name = models.CharField(max_length=50)
    shop_address = models.CharField(max_length=200)
    shop_logo = models.ImageField(upload_to=get_file_path, help_text="height = 80px Width = 80px")
    shop_banner = models.ImageField(upload_to=get_file_path, help_text="height = 1000px Width = 480px")
    contact_number = models.CharField(max_length=16, help_text="Example: +880 1626300372")
    facebook_link = models.CharField(max_length=250, help_text="Example: https://www.facebook.com/sanowardwn")
    linkedin_link = models.CharField(max_length=250, help_text="Example: https://www.linkedin.com/in/sanowar-dewan-901991227")
    twitter_link = models.CharField(max_length=250, help_text="Example: https://twitter.com/SanowarDewan5")
    instagram_link = models.CharField(max_length=250, help_text="Example: https://www.instagram.com/codeeater21/")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name="vendor", on_delete=models.CASCADE)

    class Meta:
        ordering = ['shop_name']

    def __str__(self):
        return self.shop_name


