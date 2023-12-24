from django.contrib import admin

from .models import Course, CourseFile


admin.site.register(Course)
admin.site.register(CourseFile)