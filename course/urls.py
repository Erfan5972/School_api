from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('add/', views.CourseCreateView.as_view(), name='add-course'),
    path('add-file/', views.CourseFileCreateView.as_view(), name='add-course-file'),
    path('list/', views.CourseListView.as_view(), name='list-of-courses'),
    path('retrieve-student/', views.CourseRetrieveStudentView.as_view(), name='own-courses'),
    path('retrieve-teacher/', views.CourseRetrieveTeacherView.as_view(), name='own-teachers'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)