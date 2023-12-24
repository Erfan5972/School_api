from django.db import models

from user.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    body = models.TextField()
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_id')
    students = models.ManyToManyField(User, related_name='student_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name}//{self.id}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'



class CourseFile(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='file_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='course/file/')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

