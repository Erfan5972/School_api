import os
from celery import shared_task
from django.conf import settings


@shared_task
def process_uploaded_file(file):
    file_path = os.path.join(settings.MEDIA_ROOT, 'course/file')
    print(file_path)
    with open(file_path, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return 'File processing complete'