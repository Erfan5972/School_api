from rest_framework import serializers

from . import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['name', 'title', 'body', 'teacher_id', 'students', 'id']


class CourseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseFile
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        exclude = ['created_at', 'updated_at', 'students', 'id']