from celery.decorators import periodic_task
from celery.task.schedules import crontab
from datetime import datetime, timedelta
from django.utils import timezone
from .models import DailyBusPassView

@periodic_task(run_every=crontab(hour=0, minute=0))
def delete_previous_day_objects():
    today = timezone.now().date()
    yesterday = today - timedelta(days=1)
    previous_day_bus_pass_to_delete = DailyBusPassView.objects.filter(today=yesterday)
    previous_day_bus_pass_to_delete.delete()
