from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Student, Course, Registration


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
