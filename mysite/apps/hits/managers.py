from django.utils import timezone
from datetime import timedelta
from django.db import models


class HitsLogManager(models.Manager):

    def filter_active(self, limit, *args, **kwargs):
        period = timezone.now() - timedelta(**limit)
        return self.filter(creation_date__gte=period).filter(*args, **kwargs)