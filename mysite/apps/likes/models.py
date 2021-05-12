from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Like(models.Model):   
    like          = models.BooleanField()
    user          = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='likes_user')
    creation_date = models.DateTimeField(auto_now_add=True)
    content_type  = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='likes_object')                             
    object_id     = models.PositiveIntegerField() 
    object        = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '%s - %s' % (self.object, 'Like' if self.like else 'Dislike')

    class Meta:
        get_latest_by = 'creation_date'