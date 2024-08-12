from rest_framework import serializers
from school.models import Student, Course, Registration
from school.validators import (
    invalid_cpf, invalid_name, invalid_cellphone
)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if invalid_cpf(data["cpf"]):
            raise serializers.ValidationError({
                "cpf": "CPF must be valid"
            })

        if invalid_name(data["name"]):
            raise serializers.ValidationError({
                "name": "Name must only contain letters"
            })

        if invalid_cellphone(data["cellphone"]):
            raise serializers.ValidationError({
                "cellphone": "Cellphone must follow the model: 99 99999-9999"
            })

        return data


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RegistratioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class ListRegistrationsStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()


class ListRegistrationsCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Registration
        fields = ['student_name']
