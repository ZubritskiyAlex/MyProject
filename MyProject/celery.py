import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')

app = Celery('MyProject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule ={
    'send_message':{
        'task':'MyProject.tasks.send_message',
        'shedule': 60.0
    }
}