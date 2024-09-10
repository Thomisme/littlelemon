from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import MenuItem
from ..serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Initialize the APIClient
        self.client = APIClient()

        # Create test instances of Menu
        self.menu1 = MenuItem.objects.create(title="Burger", price=5.99, inventory=50)
        self.menu2 = MenuItem.objects.create(title="Pizza", price=8.99, inventory=30)
        self.menu3 = MenuItem.objects.create(title="Pasta", price=7.99, inventory=20)

    def test_get_all_menus(self):
        # Send a GET request to the menu list endpoint
        response = self.client.get('/menus/')

        # Retrieve all Menu objects and serialize them
        menus = MenuItem.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response data matches the serialized data
        self.assertEqual(response.data, serializer.data)