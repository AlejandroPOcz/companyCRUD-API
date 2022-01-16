"""CRUD app Tests"""

# Django
from django.test import TestCase
from django.urls import reverse

# DRF
from rest_framework import status

# Local Apps
from .models import Company


class CompanyTestCase(TestCase):
    def setUp(self):
        Company.objects.create(
            name='Twitter',
            description='Social Media Company',
            symbol='TWTR'
        )

    def test_home(self):
        """
        Ensure we can access to the home Url.
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)

    def test_list_companies(self):
        """
        Ensure we can access to the list companies view.
        """
        response = self.client.get('/company-api/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_detail_company(self):
        """
        Ensure we can see a company object detail.
        """
        test_id = Company.objects.first().id.__str__()
        response = self.client.get(f'/company-api/detail/{test_id}')
        data = {
            "id": Company.objects.first().id.__str__(),
            "name": Company.objects.first().name,
            "description": Company.objects.first().description,
            "symbol": Company.objects.first().symbol,
            "market_values": Company.objects.first().market_values,
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, data)

    def test_create_company(self):
        """
        Ensure we can create a new company object.
        """
        url = reverse('company:company-create')
        data = {
            'name': 'Amazon',
            'description': 'Online Store Company',
            'symbol': 'AMZN'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 2)

    def test_delete_company(self):
        """
        Ensure we can see a company object detail.
        """
        test_id = Company.objects.first().id.__str__()
        response = self.client.delete(f'/company-api/delete/{test_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Company.objects.first(), None)
