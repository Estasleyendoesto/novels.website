from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .managers import HitsLogManager


class Hit(models.Model):
    hits         = models.PositiveIntegerField(default=0)
    last_hit     = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='hits_object')                             
    object_id    = models.PositiveIntegerField() 
    object       = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '%s - %s' % (self.object, self.hits)

    class Meta:
        unique_together = ('content_type', 'object_id')
        get_latest_by   = 'last_hit'


class HitsLog(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    ip            = models.CharField(max_length=45, editable=False)
    session       = models.CharField(max_length=40, editable=False)
    user_agent    = models.CharField(max_length=255, editable=False)
    user          = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, editable=False)
    hit           = models.ForeignKey('Hit', on_delete=models.CASCADE, editable=False)
    objects       = HitsLogManager()

    def __str__(self):
        return '%s - %s' % (self.hit.object, self.ip)

    class Meta:
        get_latest_by = 'creation_date'


class BlacklistIP(models.Model):
    ip = models.CharField(max_length=45, unique=True)


class BlacklistUA(models.Model):
    user_agent = models.CharField(max_length=255, unique=True)