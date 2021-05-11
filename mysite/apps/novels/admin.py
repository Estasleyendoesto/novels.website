from django.contrib import admin
from .models import Novel, Likes

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    pass

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    pass
