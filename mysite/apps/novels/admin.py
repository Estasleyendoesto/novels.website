from django.contrib import admin
from .models import Novel

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'pk', 'creation_date', 'last_update')