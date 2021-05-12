from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from ..hits.models import Hit
from ..likes.models import Like

class Novel(models.Model):
    title         = models.CharField(max_length=180, null=False, blank=False)

    TYPE_CHOICES = [
        ('LN', 'Light novel'),  
        ('WN', 'Web novel'),
    ]
    STRUCTURE_CHOICES = [
        ('VOL', 'Volumes'),
        ('ARC', 'Arcs'),
        ('CHA', 'Chapters'),
    ]

    type          = models.CharField(max_length=2, null=False, choices=TYPE_CHOICES ,default=TYPE_CHOICES[0][0], verbose_name='Tipo')
    structure     = models.CharField(max_length=3, null=False, choices=STRUCTURE_CHOICES, default=STRUCTURE_CHOICES[0][0], verbose_name='Estructura')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    last_update   = models.DateTimeField(auto_now=True)
    likes         = GenericRelation(Like, related_query_name='novel')
    hits          = GenericRelation(Hit, related_query_name='novel')

    def __str__(self):
        return self.title


class Distro(models.Model):
    pass


class Chapter(models.Model):
    pass


class Picture(models.Model):
    pass