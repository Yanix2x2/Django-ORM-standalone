from django.utils import timezone
from datetime import timedelta


def get_duration(visit):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at
    return timezone.now() - timezone.localtime(visit.entered_at)


def format_duration(duration):
    hour = 3600
    minute = 60
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // hour
    minutes = (total_seconds % hour) // minute
    return f'{hours:02d}:{minutes:02d}'


def is_visit_long(visit, minutes=60):
    return get_duration(visit) > timedelta(minutes=minutes)
