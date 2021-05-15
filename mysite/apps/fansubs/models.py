from django.db import models

class Fansub(models.Model):
    pass

class Membership(models.Model):
    pass

class Contrib(models.Model):
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)