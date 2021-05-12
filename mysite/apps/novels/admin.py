from django.contrib import admin
from .models import Novel

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    pass