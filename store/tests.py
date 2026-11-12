from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from .models import Collection, Customer, Product


class ProductListTests(APITestCase):
    def setUp(self):
        collection = Collection.objects.create(title="Drinks")
        self.product = Product.objects.create(
            title="Raspberry syrup",
            slug="raspberry-syrup",
            description="Raspberry syrup",
            unit_price=10,
            inventory=5,
            collection=collection,
        )

    def test_returns_serialized_products(self):
        response = self.client.get("/store/products/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], self.product.pk)
        self.assertEqual(response.data[0]["title"], self.product.title)


class CustomerMeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="customer")
        self.client.force_authenticate(user=self.user)

    def test_returns_404_when_customer_profile_does_not_exist(self):
        response = self.client.get("/store/customers/me/")

        self.assertEqual(response.status_code, 404)

    def test_returns_the_customer_profile(self):
        customer = Customer.objects.create(
            id=self.user.pk,
            first_name="Test",
            last_name="Customer",
            email="customer@example.com",
            phone="123456789",
        )

        response = self.client.get("/store/customers/me/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], customer.pk)
        self.assertEqual(response.data["email"], customer.email)

    def test_requires_authentication(self):
        self.client.force_authenticate(user=None)

        response = self.client.get("/store/customers/me/")

        self.assertEqual(response.status_code, 401)
