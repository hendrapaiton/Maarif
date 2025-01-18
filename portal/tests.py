from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from time import sleep

class LoginAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.login_url = reverse('login')

#     def test_login_success(self):
#         response = self.client.post(self.login_url, {'username': self.username, 'password': self.password})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('access', response.data)
#         self.assertIn('refresh', response.data)

#     def test_login_failure(self):
#         response = self.client.post(self.login_url, {'username': self.username, 'password': 'wrongpassword'})
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertNotIn('access', response.data)
#         self.assertNotIn('refresh', response.data)

# class TokenExpirationTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.login_url = reverse('login')
#         self.protected_url = reverse('protected-endpoint')

#     def test_access_token_expiration(self):
#         response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         access_token = response.data['access']
#         sleep(15)
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
#         response = self.client.get(self.protected_url)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# class ProtectedEndpointTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.protected_url = reverse('protected-endpoint')

#     def test_protected_endpoint_without_login(self):
#         response = self.client.get(self.protected_url)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class TokenRefreshTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.login_url = reverse('access_token')
        self.refresh_url = reverse('refresh_token')
        self.protected_url = reverse('protected-endpoint')

    def test_refresh_token(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        access_token = response.data['access']
        refresh_token = response.data['refresh']
        sleep(15)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        self.client.credentials()
        response = self.client.post(self.refresh_url, {'refresh': refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_access_token = response.data['access']
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + new_access_token)
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
