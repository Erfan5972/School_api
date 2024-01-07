from course import models
from course.apis import serializers
from .tasks import process_uploaded_file
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CourseCreateView(generics.CreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseFileCreateView(generics.GenericAPIView):
    queryset = models.CourseFile.objects.all()
    serializer_class = serializers.CourseFileSerializer
    permission_classes = [IsAuthenticated]


    def post(self, request):
        file = request.FILES
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        process_uploaded_file.delay(file)

        return Response({'message': 'File uploaded successfully'})



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