import os
import django
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

from config.settings import DEBUG

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

app = Celery('config')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

minute = '*' if DEBUG else '*/5'

app.conf.beat_schedule = {
    'calculate_delivery': {
        'task': 'applications.package.tasks.period_update_delivery',
        'schedule': crontab(minute=minute),
    },
}
