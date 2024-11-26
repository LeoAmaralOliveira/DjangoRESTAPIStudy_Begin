from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Student


class StudentsUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', password='admin'
        )
        self.url = reverse('Students-list')
        self.client.force_authenticate(self.user)
        self.student_01 = Student.objects.create(
            name='Student One',
            email='test@endpoint.com',
            cpf='92838301055',
            born_date='2000-01-01',
            cellphone='99 99999-9999'
        )
        self.student_02 = Student.objects.create(
            name='Student Two',
            email='test@endpoint.com',
            cpf='14592564090',
            born_date='2000-01-01',
            cellphone='99 99999-9999'
        )

    def test_request_get_list_students(self):
        """Test Students GET request"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
