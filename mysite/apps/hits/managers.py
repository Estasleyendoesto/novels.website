from django.utils import timezone
from datetime import timedelta
from django.db import models


class HitsLogManager(models.Manager):

    def filter_active(self, limit):
        period = timezone.now() - timedelta(**limit)
        return self.filter(created__gte=period)