from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory
from .models import Package, PackageType


class PackageTypeTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.clothing_type = PackageType.objects.create(name='clothing')
        self.electronics_type = PackageType.objects.create(name='electronics')
        self.other_type = PackageType.objects.create(name='other')

    def test_package_type_str(self):
        self.assertEqual(str(self.clothing_type), 'Одежда')
        self.assertEqual(str(self.electronics_type), 'Электроника')
        self.assertEqual(str(self.other_type), 'Разное')


class PackageTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.clothing_type = PackageType.objects.create(name='clothing')
        self.package_data = {
            'title': 'Test Package',
            'weight': 2.5,
            'type': self.clothing_type.name,
            'user_session': 'test_session',
            'cost': 50,
        }

    def test_create_package(self):
        url = reverse('package')
        response = self.client.post(url, self.package_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Package.objects.count(), 1)
        package = Package.objects.first()
        self.assertEqual(package.title, 'Test Package')
