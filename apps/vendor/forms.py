from django.forms import ModelForm
from apps.product.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'quantity', 'small_description', 'description', 'image']