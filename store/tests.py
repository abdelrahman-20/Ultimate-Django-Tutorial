# from django.test import TestCase
# from .models import Collection, Product


# class ProductCollectionLinkTests(TestCase):
#     def setUp(self):
#         self.collection = Collection.objects.create(title="Drinks")
#         self.product = Product.objects.create(
#             title="Island Oasis - Raspberry",
#             description="Raspberry syrup",
#             unit_price=84.64,
#             inventory=10,
#             collection=self.collection,
#         )

#     def test_product_list_returns_collection_hyperlink(self):
#         response = self.client.get("/store/products/")

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(
#             response.data[0]["collection"],
#             f"http://testserver/store/collections/{self.collection.pk}/",
#         )

#     def test_product_details_returns_collection_hyperlink(self):
#         response = self.client.get(f"/store/products/{self.product.pk}/")

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(
#             response.data["collection"],
#             f"http://testserver/store/collections/{self.collection.pk}/",
#         )

#     def test_product_list_rejects_invalid_post_data(self):
#         response = self.client.post("/store/products/", data={}, format="json")

#         self.assertEqual(response.status_code, 400)
