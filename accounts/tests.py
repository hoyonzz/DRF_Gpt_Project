from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User


class AccountTests(APITestCase):
    def test_create_account(self):
        url = reverse('account_create')
        data = {'username': 'testuser', 'password':'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')