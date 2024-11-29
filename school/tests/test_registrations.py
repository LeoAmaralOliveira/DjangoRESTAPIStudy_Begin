from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Student, Course, Registration
from school.serializers import RegistratioSerializer


class RegistrationsUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', password='admin'
        )
        self.url = reverse('Registrations-list')
        self.client.force_authenticate(self.user)
        self.student_registration = Student.objects.create(
            name='Testing Test 2',
            email='test2@test.com',
            cpf='57520711005',
            born_date='2000-12-31',
            cellphone='11 11111-1111'
        )
        self.course_registration = Course.objects.create(
            code='Test03',
            description='Test03',
            level='I'
        )
        self.course_registration_02 = Course.objects.create(
            code='Test04',
            description='Test04',
            level='I'
        )
        self.registration_01 = Registration.objects.create(
            student=self.student_registration,
            course=self.course_registration,
            period='M'
        )
        self.registration_02 = Registration.objects.create(
            student=self.student_registration,
            course=self.course_registration_02,
            period='M'
        )

    def test_request_get_list_registrations(self):
        """Test Registrations GET request"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_a_registration(self):
        """Test Registrations GET a item request"""
        response = self.client.get(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        registration_data = Registration.objects.get(pk=1)
        serialized_registration_data = RegistratioSerializer(instance=registration_data).data
        self.assertEqual(response.data, serialized_registration_data)

    def test_request_post_registration(self):
        """Test Registration POST request"""
        data = {
            'student': self.student_registration.pk,
            'course': self.course_registration_02.pk,
            'period': 'M'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_request_delete_registration(self):
        """Test of DELETE Registration request"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_request_put_registration(self):
        """Test Registration PUT request"""
        data = {
            'student': self.student_registration,
            'course': self.course_registration.pk,
            'period': 'N'
        }
        response = self.client.put(f'{self.url}1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
