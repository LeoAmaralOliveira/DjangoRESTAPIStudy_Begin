from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Course


class CoursesUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', password='admin'
        )
        self.url = reverse('Courses-list')
        self.client.force_authenticate(self.user)
        self.course_01 = Course.objects.create(
            code='Test01',
            description='Test',
            level='B'
        )
        self.course_02 = Course.objects.create(
            code='Test02',
            description='Test',
            level='B'
        )

    def test_request_get_list_courses(self):
        """Test Courses GET request"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
