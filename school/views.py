from school.models import Student, Course, Registration
from school.serializers import (
    StudentSerializer,
    CourseSerializer,
    RegistratioSerializer,
    ListRegistrationsStudentSerializer,
    ListRegistrationsCourseSerializer
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationViewSet(ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistratioSerializer


class ListRegistrationStudent(ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(student=self.kwargs['pk'])
        return queryset

    serializer_class = ListRegistrationsStudentSerializer


class ListRegistrationCourse(ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(course=self.kwargs['pk'])
        return queryset

    serializer_class = ListRegistrationsCourseSerializer
