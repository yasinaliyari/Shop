from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from app.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "description", "price", "stock"]

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price > 1000:
            raise ValidationError("Product is too expensive")
        return price
