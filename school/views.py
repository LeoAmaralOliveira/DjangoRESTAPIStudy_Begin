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
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class StudentViewSet(ModelViewSet):
    """
    ViewSet Description:
    - CRUD Students endpoint.

    Ordenation fields:
    - name: allow order results by name.

    Search fields:
    - name: allow search results by name.
    - cpf: allow search results by CPF.

    Allowed HTTP Methods:
    - GET, POST, PUT, PATCH, DELETE

    Serializer Class:
    - StudentSerializer: is used to serialize and deserialize data.
    - If API version is 'v2' then the StudentSerializerV2 is used.
    """
    queryset = Student.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf',]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer


class CourseViewSet(ModelViewSet):
    """
    ViewSet Description:
    - CRUD Courses endpoint.

    Allowed HTTP Methods:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RegistrationViewSet(ModelViewSet):
    """
    ViewSet Description:
    - CRUD Registration endpoint.

    Allowed HTTP Methods:
    - GET, POST

    Throttle Classes:
    - RegistrationAnonRateThrottle: rate limit for anonymous users.
    - UserRateThrottle: rate limit for authenticated users.
    """
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
