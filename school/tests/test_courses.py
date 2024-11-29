from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Course
from school.serializers import CourseSerializer


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

    def test_request_get_a_course(self):
        """Test Courses GET a item request"""
        response = self.client.get(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        course_data = Course.objects.get(pk=1)
        serialized_course_data = CourseSerializer(instance=course_data).data
        self.assertEqual(response.data, serialized_course_data)

    def test_request_post_course(self):
        """Test Course POST request"""
        data = {
            'code': 'test-post',
            'description': 'Test',
            'level': 'B'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_request_delete_course(self):
        """Test of DELETE Course request"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_request_put_course(self):
        """Test Course PUT request"""
        data = {
            'code': 'test-put',
            'description': 'TestPut',
            'level': 'B'
        }
        response = self.client.put(f'{self.url}1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
