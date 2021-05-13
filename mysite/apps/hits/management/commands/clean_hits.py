from django.core.management.base import BaseCommand, CommandError

from django.conf import settings
from django.utils import timezone
from datetime import timedelta

from ...models import HitsLog

class Command(BaseCommand):
    help = 'Puede ejecutarse como un cronjob o directamente desde manage.py para pugar registros de la DB'

    def handle(self, *args, **options):
        limit = getattr(settings, 'KEEP_HITSLOGS_IN_DB', {'days': 30})
        period = timezone.now() - timedelta(**limit)
        hits_logs = HitsLog.objects.filter(creation_date__lt=period)
        deletions = hits_logs.count()
        hits_logs.delete()
        self.stdout.write( self.style.SUCCESS('Se han eliminado %s HitsLogs' % deletions) )