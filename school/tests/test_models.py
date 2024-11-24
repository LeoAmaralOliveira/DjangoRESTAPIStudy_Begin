from django.test import TestCase
from school.models import Student, Course, Registration


class ModelStudentTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name='Testing Test',
            email='test@test.com',
            cpf='97729017067',
            born_date='2000-01-01',
            cellphone='99 99999-9999'
        )

    def test_students_model_attr(self):
        """This test verifies students model attributes"""
        self.assertEqual(self.student.name, 'Testing Test')
        self.assertEqual(self.student.email, 'test@test.com')
        self.assertEqual(self.student.cpf, '97729017067')
        self.assertEqual(self.student.born_date, '2000-01-01')
        self.assertEqual(self.student.cellphone, '99 99999-9999')


class ModelCourseTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            code='Test',
            description='Test',
            level='B'
        )

    def test_course_model_attr(self):
        """This test verifies course model attributes"""
        self.assertEqual(self.course.code, 'Test')
        self.assertEqual(self.course.description, 'Test')
        self.assertEqual(self.course.level, 'B')


class ModelRegistrationTestCase(TestCase):
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
        self.registration = Registration.objects.create(
            student=self.student_registration,
            course=self.course_registration,
            period='M'
        )

    def test_registration_model_attr(self):
        """This test verifies registration model attributes"""
        self.assertEqual(self.registration.student, self.student_registration)
        self.assertEqual(self.registration.course, self.course_registration)
        self.assertEqual(self.registration.period, 'M')
