import unittest
from django.test import TestCase
from .models import Product


# Create your tests here.
class ProductsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create a product
        test_product = Product.objects.create(
            barcode='98765',
            name='product name',
            category='product category',
            description='product description',
            unit_cost=10.0,
            quantity_in_stock=100.0
        )
        test_product.save()

    def test_product_content(self):
        product = Product.objects.get(id=1)
        barcode = product.barcode
        name = product.name
        category = product.category
        description = product.description
        unitCost = product.unit_cost
        quantityInStock = product.quantity_in_stock
        self.assertEqual(barcode, '98765')
        self.assertEqual(name, 'product name')
        self.assertEqual(category, 'product category')
        self.assertEqual(description, 'product description')
        self.assertEqual(unitCost, 10.0)
        self.assertEqual(quantityInStock, 100.0)

# Product.objects.get(name='product name').delete()