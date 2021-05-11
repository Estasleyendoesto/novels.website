from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

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
    likes         = GenericRelation('Likes', related_query_name='novel')

    def __str__(self):
        return self.title

    
class Likes(models.Model):   
    like = models.BooleanField(null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='likes_user')

    object_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='likes_object')                             
    object_id = models.PositiveIntegerField() 
    object    = GenericForeignKey('object_content_type', 'object_id')

    def __str__(self):
        return '%s - %s' % (self.object, 'Like' if self.like else 'Dislike')

    def exists(self):
        r = Likes.objects.filter(user=self.user, object=self.object).first()
        if r:
            return True
        else:
            return False

    # Esto está roto, corregir el problema que los likes tienen que ser únicos por usuario a un determianado objeto
    # No funciona novela.likes.all(), hay que corregir


class Distro(models.Model):
    pass


class Chapter(models.Model):
    pass


class Picture(models.Model):
    pass