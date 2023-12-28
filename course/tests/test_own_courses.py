from django.contrib.auth import get_user_model
from django.urls import reverse

from .. models import Course

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from model_bakery import baker


class TestOwnCourses(APITestCase):
    def setUp(self):
        self.user = baker.make(get_user_model())
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.refresh.access_token}')
        self.Course = baker.make(Course, students=[self.user], _quantity=10)

    def test_own_courses(self):
        url = reverse('course:own-courses')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)