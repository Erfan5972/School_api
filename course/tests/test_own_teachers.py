from django.contrib.auth import get_user_model
from django.urls import reverse

from .. models import Course

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from model_bakery import baker


class TestOwnTeachers(APITestCase):
    def setUp(self):
        self.user = baker.make(get_user_model())
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.refresh.access_token}')
        self.Course = baker.make(Course, teacher_id=self.user, _quantity=10)

    def test_own_teachers(self):
        url = reverse('course:own-teachers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)