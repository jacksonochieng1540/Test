from django.test import TestCase
from django.urls import reverse
from .models import Product
from .forms import ProductForm
from rest_framework.test import APITestCase
from rest_framework import status


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Laptop", price=1000)

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(float(self.product.price), 1000.0)

class ProductFormTest(TestCase):
    def test_valid_form(self):
        data = {'name': 'Phone', 'price': 500, 'description': 'Smartphone'}
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': '', 'price': 500}
        form = ProductForm(data=data)
        self.assertFalse(form.is_valid())

# --- View Tests ---
class ProductViewTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Laptop", price=1000)

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Laptop")
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_product_create_view_get(self):
        response = self.client.get(reverse('product_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_form.html')

# --- API Tests ---
class ProductAPITest(APITestCase):
    def setUp(self):
        Product.objects.create(name="Laptop", price=1000)

    def test_get_api_products(self):
        url = reverse('product_api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
