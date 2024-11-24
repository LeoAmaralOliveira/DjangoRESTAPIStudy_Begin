from django.test import TestCase
from school.models import Student, Course, Registration
from school.serializers import (
    StudentSerializer,
    StudentSerializerV2,
    CourseSerializer,
    RegistratioSerializer,
    ListRegistrationsStudentSerializer,
    ListRegistrationsCourseSerializer
)


class StudentSerializerTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            name='Testing Test',
            email='test@test.com',
            cpf='97729017067',
            born_date='2000-01-01',
            cellphone='99 99999-9999'
        )
        self.student_serializer = StudentSerializer(instance=self.student)

    def test_student_serializer_data_keys(self):
        """This test verify the return keys of student serializer"""
        data = self.student_serializer.data
        self.assertEqual(
            set(data.keys()),
            set(['id', 'name', 'email', 'cpf', 'born_date', 'cellphone'])
        )

    def test_student_serializer_data_values(self):
        """This test verify the return values of student serializer"""
        data = self.student_serializer.data
        self.assertEqual(data['name'], self.student.name)
        self.assertEqual(data['email'], self.student.email)
        self.assertEqual(data['cpf'], self.student.cpf)
        self.assertEqual(data['born_date'], self.student.born_date)
        self.assertEqual(data['cellphone'], self.student.cellphone)


class StudentSerializerV2TestCase(TestCase):
    def setUp(self):
        self.student = Student(
            name='Testing TestV2',
            email='testv2@test.com',
            cpf='66467342089',
            born_date='2000-01-01',
            cellphone='99 99999-9999'
        )
        self.student_serializer_v2 = StudentSerializerV2(instance=self.student)

    def test_student_serializer_v2_data_keys(self):
        """This test verify the return keys of student serializer v2"""
        data = self.student_serializer_v2.data
        self.assertEqual(
            set(data.keys()),
            set(['id', 'name', 'email', 'cellphone'])
        )

    def test_student_serializer_v2_data_values(self):
        """This test verify the return values of student serializer v2"""
        data = self.student_serializer_v2.data
        self.assertEqual(data['name'], self.student.name)
        self.assertEqual(data['email'], self.student.email)
        self.assertEqual(data['cellphone'], self.student.cellphone)


class CourseSerializerTestCase(TestCase):
    def setUp(self):
        self.course = Course(
            code='Test',
            description='Test',
            level='B'
        )
        self.course_serializer = CourseSerializer(instance=self.course)

    def test_course_serializer_data_keys(self):
        """This test verify the return keys of course serializer"""
        data = self.course_serializer.data
        self.assertEqual(
            set(data.keys()),
            set(['id', 'code', 'description', 'level'])
        )

    def test_course_serializer_data_values(self):
        """This test verify the return values of course serializer"""
        data = self.course_serializer.data
        self.assertEqual(data['code'], self.course.code)
        self.assertEqual(data['description'], self.course.description)
        self.assertEqual(data['level'], self.course.level)


class RegistratioSerializerTestCase(TestCase):
    def setUp(self):
        self.student_registration = Student.objects.create(
            name='Testing Test 2',
            email='test2@test.com',
            cpf='57520711005',
            born_date='2000-12-31',
            cellphone='11 11111-1111'
        )
        self.course_registration = Course.objects.create(
            code='Test2',
            description='Test2',
            level='I'
        )
        self.registration = Registration(
            student=self.student_registration,
            course=self.course_registration,
            period='M'
        )
        self.registration_serializer = RegistratioSerializer(instance=self.registration)

    def test_registration_serializer_data_keys(self):
        """This test verify the return keys of registration serializer"""
        data = self.registration_serializer.data
        self.assertEqual(
            set(data.keys()),
            set(['id', 'student', 'course', 'period'])
        )

    def test_registration_serializer_data_values(self):
        """This test verify the return values of registration serializer"""
        data = self.registration_serializer.data
        self.assertEqual(data['student'], self.registration.student.id)
        self.assertEqual(data['course'], self.registration.course.id)
        self.assertEqual(data['period'], self.registration.period)


class ListRegistrationsStudentSerializerTestCase(TestCase):
    def setUp(self):
        self.student_registration = Student.objects.create(
            name='Testing Test 3',
            email='test3@test.com',
            cpf='57520711005',
            born_date='2000-12-31',
            cellphone='22 22222-2222'
        )
        self.course_registration = Course.objects.create(
            code='Test3',
            description='Test3',
            level='A'
        )
        self.registration = Registration(
            student=self.student_registration,
            course=self.course_registration,
            period='M'
        )
        self.list_registrations_student_serializer = ListRegistrationsStudentSerializer(instance=self.registration)

    def test_list_registrations_student_serializer_data_keys(self):
        """This test verify the return keys of list student registrations serializer"""
        data = self.list_registrations_student_serializer.data
        self.assertEqual(
            set(data.keys()),
            set(['course', 'period'])
        )

    def test_list_registrations_student_serializer_data_values(self):
        """This test verify the return values of list student registrations serializer"""
        data = self.list_registrations_student_serializer.data
        self.assertEqual(data['course'], self.registration.course.description)
        self.assertEqual(data['period'], 'Morning')


class ListRegistrationsCourseSerializerTestCase(TestCase):
    def setUp(self):
        self.student_registration = Student.objects.create(
            name='Testing Test 4',
            email='test4@test.com',
            cpf='44413146042',
            born_date='2000-12-31',
            cellphone='33 33333-3333'
        )
        self.course_registration = Course.objects.create(
            code='Test4',
            description='Test4',
            level='B'
        )
        self.registration = Registration(
            student=self.student_registration,
            course=self.course_registration,
            period='N'
        )
        self.list_registrations_course_serializer = ListRegistrationsCourseSerializer(instance=self.registration)

    def test_list_registrations_course_serializer_data_keys(self):
        """This test verify the return keys of list course registrations serializer"""
        data = self.list_registrations_course_serializer.data
        self.assertEqual(
            set(data.keys()),
            set(['student_name'])
        )

    def test_list_registrations_course_serializer_data_values(self):
        """This test verify the return values of list course registrations serializer"""
        data = self.list_registrations_course_serializer.data
        self.assertEqual(data['student_name'], self.registration.student.name)
