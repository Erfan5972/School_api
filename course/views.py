from . import serializers
from . import models


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class CourseCreateView(generics.CreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseFileCreateView(generics.CreateAPIView):
    queryset = models.CourseFile.objects.all()
    serializer_class = serializers.CourseFileSerializer
    permission_classes = [IsAuthenticated]


class CourseListView(generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseListSerializer
    permission_classes = [IsAuthenticated]


class CourseRetrieveStudentView(generics.ListAPIView):
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = models.Course.objects.filter(students=user_id)
        return queryset


class CourseRetrieveTeacherView(generics.ListAPIView):
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = models.Course.objects.filter(teacher_id_id=user_id)
        return queryset