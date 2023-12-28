from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from .. models import Course
from model_bakery import baker


class TestAddFileCourses(APITestCase):
    def setUp(self):
        self.user = baker.make(get_user_model())
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.refresh.access_token}')
        self.course = baker.make(Course)
        file_content = b'Test file content'
        self.file = SimpleUploadedFile('test_file.txt', file_content, content_type='text/plain')


    def test_user_add_course_file(self):
        url = reverse('course:add-course-file')
        data = {
            'title': 'math_file',
            'body': 'math_file',
            'course_id': self.course.id,
            'file': self.file
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Course.objects.all().count(), 1)


    def test_invalid_user_add_course_file(self):
        url = reverse('course:add-course-file')
        data = {}
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertGreaterEqual(Course.objects.all().count(), 0)

