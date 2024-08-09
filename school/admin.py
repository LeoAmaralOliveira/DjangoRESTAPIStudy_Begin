from django.contrib import admin
from school.models import Student, Course, Registration


class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'born_date', 'cellphone')
    list_display_links = ('id', 'name',)
    list_per_page = 20
    search_fields = ('name',)


admin.site.register(Student, Students)


class Courses(admin.ModelAdmin):
    list_display = ('id', 'code', 'description')
    list_display_links = ('id', 'code',)
    search_fields = ('code',)


admin.site.register(Course, Courses)


class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id',)


admin.site.register(Registration, Registrations)
