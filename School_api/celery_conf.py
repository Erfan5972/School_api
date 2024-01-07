import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'School_api.settings')
app = Celery('proj')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_url = 'redis://localhost:6379'
app.conf.result_backend = 'redis://localhost:6379'
app.conf.task_serializer = 'pickle'
app.conf.result_serializer = 'json'
app.conf.accept_content = ['application/x-python-serialize', 'json']

app.autodiscover_tasks()