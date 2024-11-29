from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Student
from school.serializers import StudentSerializer


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

    def test_request_get_a_student(self):
        """Test Students GET a item request"""
        response = self.client.get(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        student_data = Student.objects.get(pk=1)
        serialized_student_data = StudentSerializer(instance=student_data).data
        self.assertEqual(response.data, serialized_student_data)

    def test_request_post_student(self):
        """Test Student POST request"""
        data = {
            'name': 'test',
            'email': 'test@test.com',
            'cpf': '82271917034',
            'born_date': '2003-05-04',
            'cellphone': '11 99999-9999'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_request_delete_student(self):
        """Test of DELETE Student request"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_request_put_student(self):
        """Test Student PUT request"""
        data = {
            'name':'teste',
            'email':'testeput@gmail.com',
            'cpf':'42370866071',
            'born_date':'2003-05-09',
            'cellphone':'11 88888-6666'
        }
        response = self.client.put(f'{self.url}1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
