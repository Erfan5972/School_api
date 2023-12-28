from django.urls import reverse
from django.contrib.auth import get_user_model

from .. models import Course

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from model_bakery import baker


class TestAddCourses(APITestCase):
    def setUp(self):
        self.user = baker.make(get_user_model())
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.refresh.access_token}')


    def test_user_add_course(self):
        url = reverse('course:add-course')
        data = {
            'name': 'math',
            'title': 'math',
            'body': 'math',
            'teacher_id': self.user.id,
            'students': self.user.id,

        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Course.objects.all().count(), 1)

    def test_invalid_user_add_course(self):
        url = reverse('course:add-course')
        data = {}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertGreaterEqual(Course.objects.all().count(), 0)

