from school.models import Student, Course, Registration
from school.serializers import (
    StudentSerializer,
    StudentSerializerV2,
    CourseSerializer,
    RegistratioSerializer,
    ListRegistrationsStudentSerializer,
    ListRegistrationsCourseSerializer
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from school.throttles import RegistrationAnonRateThrottle


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf',]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer


class RegistrationViewSet(ModelViewSet):
    queryset = Registration.objects.all().order_by('id')
    serializer_class = RegistratioSerializer
    throttle_classes = [UserRateThrottle, RegistrationAnonRateThrottle]
    http_method_names = ["get", "post"]


class ListRegistrationStudent(ListAPIView):
    """
    View Description:
    - List Registrations by Student ID
    Parameters:
    - pk (int): Object primary identifier. Must be integer.
    """
    def get_queryset(self):
        queryset = Registration.objects.filter(student=self.kwargs['pk']).order_by('id')
        return queryset

    serializer_class = ListRegistrationsStudentSerializer


class ListRegistrationCourse(ListAPIView):
    """
    View Description:
    - List Registrations by Course ID
    Parameters:
    - pk (int): Object primary identifier. Must be integer.
    """
    def get_queryset(self):
        queryset = Registration.objects.filter(course=self.kwargs['pk']).order_by('id')
        return queryset

    serializer_class = ListRegistrationsCourseSerializer
