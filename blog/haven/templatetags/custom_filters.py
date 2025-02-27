from django import template
from datetime import timedelta
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta




register=template.Library()

@register.filter
def first_letter(value):
    if value:
        return value[:1]
    return ""


@register.filter
def custom_time_since(timestamp):
    diff = now() - timestamp
    rdelta = relativedelta(now(), timestamp)

    if diff < timedelta(minutes=1):
        return "just now"
    elif diff < timedelta(hours=1):
        return f"{int(diff.total_seconds() // 60)} minutes ago"
    elif diff < timedelta(days=1):
        hours = diff.seconds // 3600
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif diff < timedelta(days=2):
        return "1 day ago"
    elif diff < timedelta(days=30):
        return f"{diff.days} days ago"
    elif rdelta.months == 1:
        return "1 month ago"
    elif rdelta.months > 1:
        return f"{rdelta.months} months ago"
    elif rdelta.years == 1:
        return "1 year ago"
    else:
        return f"{rdelta.years} years ago"