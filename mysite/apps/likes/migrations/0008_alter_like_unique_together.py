# Generated by Django 3.2 on 2021-05-12 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0007_auto_20210513_0031'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
    ]
