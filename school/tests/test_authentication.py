from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import authenticate
from django.urls import reverse


class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', password='admin'
        )
        self.url = reverse('Students-list')

    def test_correct_authentication(self):
        """Test if authentication is correct"""
        user = authenticate(username='admin', password='admin')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_incorrect_username_authentication(self):
        """Test authentication when the username is incorrect"""
        user = authenticate(username='adm', password='admin')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_incorrect_password_authentication(self):
        """Test authentication when the password is incorrect"""
        user = authenticate(username='admin', password='adm')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_request_get_authorized(self):
        """Testing authorized authentication in request"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_unauthorized(self):
        """Testing unauthorized authentication in request"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
