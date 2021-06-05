from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):

    barcode = models.CharField(max_length=13,
                               help_text="Enter Product Barcode ")
    name = models.CharField(max_length=200,
                            help_text="Enter Product Title")
    category = models.CharField(max_length=200,
                                help_text="Enter Product Category")
    description = models.TextField(help_text="Enter Product Description")
    unit_cost = models.FloatField(help_text="Enter Product Unit Cost")
    quantity_in_stock = models.FloatField(help_text="Enter Product Quantity")
    creator = models.ForeignKey(to=User,
                                max_length=20,
                                help_text="Enter Creator Name",
                                on_delete=models.SET_NULL,
                                null=True)

    def __str__(self):
        return self.name
